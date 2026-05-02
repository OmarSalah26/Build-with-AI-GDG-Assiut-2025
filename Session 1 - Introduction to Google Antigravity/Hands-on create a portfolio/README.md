# My Portfolio

Built with [Antigravity](https://antigravity.so) & Google Gemini

---

## 📁 Folder Structure

```
my-portfolio/
├── assets/
│   ├── images/      → hero image, project screenshots (1200×630 px hero, 800×500 px thumbnails, 400×400 px profile)
│   ├── icons/       → favicon, social icons, tech-stack logos
│   └── fonts/       → any custom font files
├── projects/
│   ├── project-1.md → one file per project (see template below)
│   └── project-2.md
├── content/
│   ├── bio.txt       → your professional bio (see prompt below)
│   ├── skills.txt    → raw list of your skills (see prompt below)
│   └── experience.txt→ work, internships, education
└── README.md         → this file
```

---

## ✦ Gemini Prompt Templates

Copy these prompts into Gemini, fill in the `[brackets]`, and paste the output into the matching file.

---

### 🟡 Bio Prompt → paste result into `content/bio.txt`

```
Write a 3-sentence professional bio for [Your Name], a [Your Role] at [Your Institution]
specialising in [your field, e.g. Machine Learning, NLP, Computer Vision].
Tone: confident, approachable, third-person.
```

---

### 🟡 Project Description Prompt → paste result into `projects/project-1.md`

```
Here is my raw project README:

[paste your raw notes or README here]

Rewrite it as a 2-sentence portfolio card description highlighting the problem
solved and the impact. Avoid jargon. Then write a longer paragraph (4–6
sentences) for the full project page.
```

---

### 🟡 Skills Grouping Prompt → paste result into `content/skills.txt`

```
Group these skills into 3 logical categories for a portfolio skills section,
and suggest a recruiter-friendly label for each group:

[list your skills here, e.g. Python, TensorFlow, Pandas, React, Git, Docker]
```

---

### 🟡 Hero Headline Prompt → use on your Antigravity hero section

```
Write 5 hero headline options for a portfolio.
Owner: [Your Name], [Your Role].
Focus: [your specialisation, e.g. AI & Machine Learning].
Keep each under 10 words.
```

---

### 🟡 SEO Meta Prompt → paste into Antigravity SEO settings

```
Write a page title (max 60 characters) and meta description (max 155
characters) for an AI portfolio belonging to [Your Name], [Your Role]
at [Your Institution], specialising in [your field].
```

---

## 📄 Project File Template

Use this template for every file inside `projects/`:

```markdown
# Project Name

## Problem
What challenge or question did this project address?

## Approach
How did you tackle it? What tools, models, or methods did you use?

## Result
What was the outcome? Include numbers where possible (e.g. "accuracy improved by 18%").

## Tech Stack
- Language: 
- Libraries: TensorFlow, Pandas, Scikit-learn
- Tools: Jupyter, Google Colab, Git

## Links
- 🔗 GitHub: 
- 🚀 Live Demo: https://...
```

---

## ✅ Pre-Publish Checklist

Before going live, make sure:

- [ ] All links work (GitHub, demos, email)
- [ ] Mobile layout tested (iPhone + Android)
- [ ] Profile photo is professional & clear
- [ ] No spelling or grammar errors (run through Gemini)
- [ ] No placeholder "Lorem ipsum…" text left
- [ ] Hero headline is specific (not just "Welcome to my portfolio")
- [ ] At least 2 real projects with screenshots
- [ ] Social handle [@yourusername] linked prominently
- [ ] Favicon is set (not the default Antigravity icon)
- [ ] Custom domain connected (or clean subdomain)

---

## ❌ Don'ts

- Don't list every project — curate ruthlessly (3–5 strong ones)
- Don't use clip-art or generic stock photos
- Don't publish AI-generated content without reviewing it
- Don't use more than 2 font families
- Don't leave placeholder text visible
- Don't forget alt-text on images (accessibility)

---

*Enactus BUA · Portfolio Building Session*
