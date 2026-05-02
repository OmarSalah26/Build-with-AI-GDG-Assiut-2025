import { useState } from 'react'
import './index.css'

const API_URL = "http://localhost:8000/api"

function App() {
  const [repoInput, setRepoInput] = useState('')
  const [repoName, setRepoName] = useState('')
  const [files, setFiles] = useState([])
  const [totalFiles, setTotalFiles] = useState(0)
  
  const [status, setStatus] = useState('idle') // idle, scanning, ready, refactoring, done
  const [error, setError] = useState(null)
  
  const [fileStatuses, setFileStatuses] = useState({}) // path -> status (pending, processing, success, error)
  const [refactoredData, setRefactoredData] = useState({}) // path -> { original, refactored, tests, issues }
  
  const [selectedFile, setSelectedFile] = useState(null)
  const [branchName, setBranchName] = useState('enhac/AI-step-1')

  const scanRepo = async () => {
    setStatus('scanning')
    setError(null)
    try {
      const res = await fetch(`${API_URL}/scan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ repo_name: repoInput })
      })
      if (!res.ok) throw new Error(await res.text())
      
      const data = await res.json()
      setRepoName(data.repo_name)
      setFiles(data.source_files)
      setTotalFiles(data.total_files)
      
      const initialStatuses = {}
      data.source_files.forEach(f => initialStatuses[f] = 'pending')
      setFileStatuses(initialStatuses)
      
      setStatus('ready')
    } catch (err) {
      setError(err.message)
      setStatus('idle')
    }
  }

  const startRefactoring = async () => {
    setStatus('refactoring')
    setError(null)
    
    for (const file of files) {
      setFileStatuses(prev => ({...prev, [file]: 'processing'}))
      setSelectedFile(file)
      
      try {
        const res = await fetch(`${API_URL}/refactor`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ repo_name: repoName, file_path: file })
        })
        if (!res.ok) throw new Error(await res.text())
        
        const data = await res.json()
        setRefactoredData(prev => ({...prev, [file]: data}))
        setFileStatuses(prev => ({...prev, [file]: 'success'}))
      } catch (err) {
        console.error(err)
        setFileStatuses(prev => ({...prev, [file]: 'error'}))
      }
    }
    
    setStatus('done')
  }

  const pushToGithub = async () => {
    try {
      // Gather successfully refactored files
      const filesToPush = Object.keys(refactoredData).map(f => ({
        file_path: f,
        content: refactoredData[f].refactored_code
      }))
      
      if (filesToPush.length === 0) return alert("No files to push!")
      
      const res = await fetch(`${API_URL}/push`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          repo_name: repoName,
          branch_name: branchName,
          files: filesToPush
        })
      })
      if (!res.ok) throw new Error(await res.text())
      
      alert(`Successfully pushed to ${branchName}!`)
    } catch (err) {
      alert(`Error pushing: ${err.message}`)
    }
  }

  return (
    <div className="container">
      <h1>Project Sentinel</h1>
      <div className="subtitle">The Autonomous Codebase Maintenance Agency</div>

      <div className="grid grid-2">
        {/* Left Column: Controls and File List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          
          <div className="glass-panel">
            <h2>Repository Source</h2>
            <input 
              placeholder="e.g. TawadrosGamal/Hotel-reservation-system-java-" 
              value={repoInput}
              onChange={e => setRepoInput(e.target.value)}
              disabled={status !== 'idle'}
            />
            <button 
              onClick={scanRepo} 
              disabled={!repoInput || status === 'scanning' || status !== 'idle'}
            >
              {status === 'scanning' ? 'Scanning...' : 'Scan Repository'}
            </button>
            {error && <div style={{color: '#f87171', marginTop: '12px'}}>{error}</div>}
          </div>

          {(status === 'ready' || status === 'refactoring' || status === 'done') && (
            <div className="glass-panel" style={{ flexGrow: 1 }}>
              <h2>Found Files ({files.length} / {totalFiles})</h2>
              
              <ul className="file-list">
                {files.map(file => (
                  <li 
                    key={file} 
                    className={`file-item ${selectedFile === file ? 'active' : ''}`}
                    onClick={() => setSelectedFile(file)}
                  >
                    <span>{file}</span>
                    <span className={`status-badge ${fileStatuses[file]}`}>
                      {fileStatuses[file]}
                    </span>
                  </li>
                ))}
              </ul>
              
              {status === 'ready' && (
                <button onClick={startRefactoring} style={{width: '100%'}}>
                  Start Autonomous Refactoring
                </button>
              )}
              
              {status === 'done' && (
                <div style={{ marginTop: '20px', borderTop: '1px solid rgba(255,255,255,0.1)', paddingTop: '20px' }}>
                  <h3>Push to GitHub</h3>
                  <input 
                    value={branchName}
                    onChange={e => setBranchName(e.target.value)}
                    placeholder="Branch name"
                  />
                  <button onClick={pushToGithub} style={{width: '100%'}}>
                    Push {Object.keys(refactoredData).length} Files
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Right Column: Code Viewer */}
        <div className="glass-panel">
          <h2>Code Viewer</h2>
          {!selectedFile ? (
            <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: '40px' }}>
              Select a file to view changes
            </div>
          ) : (
            <div>
              <h3>{selectedFile}</h3>
              {refactoredData[selectedFile] ? (
                <div>
                  <div style={{ marginBottom: '16px' }}>
                    <strong style={{color: 'var(--accent)'}}>Language:</strong> {refactoredData[selectedFile].language}
                  </div>
                  
                  {refactoredData[selectedFile].issues_found?.length > 0 && (
                    <div style={{ marginBottom: '16px', background: 'rgba(248, 113, 113, 0.1)', padding: '12px', borderRadius: '8px' }}>
                      <strong style={{color: '#f87171'}}>Issues Found:</strong>
                      <ul style={{ margin: '8px 0 0 0', paddingLeft: '20px' }}>
                        {refactoredData[selectedFile].issues_found.map((issue, idx) => (
                          <li key={idx}>[{issue.severity}] {issue.issue}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  <div className="diff-view" style={{ gridTemplateColumns: '1fr' }}>
                    <div>
                      <h4 style={{color: 'var(--success)'}}>Refactored Code</h4>
                      <div className="code-block">
                        {refactoredData[selectedFile].refactored_code}
                      </div>
                    </div>
                    <div style={{marginTop: '20px'}}>
                      <h4 style={{color: 'var(--accent)'}}>Generated Tests</h4>
                      <div className="code-block">
                        {refactoredData[selectedFile].unit_tests}
                      </div>
                    </div>
                  </div>
                </div>
              ) : (
                <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: '40px' }}>
                  {fileStatuses[selectedFile] === 'processing' ? 'Agent is currently refactoring...' : 'Pending analysis'}
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
