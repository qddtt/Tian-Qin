# Qin Tian - Academic Personal Website

This repository contains the source for Qin Tian's academic personal website:

https://tianqin.netlify.app/

The site is built with Hugo and Hugo Blox. It is designed as an English-first PhD application and research portfolio site, highlighting:

- Model Predictive Control and trajectory tracking for autonomous mining trucks
- Field experience with unmanned mining truck control systems
- Publications and projects in autonomous driving, MPC, fuzzy-PID, and vehicle-road-cloud integration
- A forward-looking research direction toward reinforcement learning, learning-based control, and data-driven autonomous systems

## Local Development

This project uses a pinned Hugo version to match Netlify:

```powershell
D:\博士入学前\工具链\hugo-0.136.5\hugo.exe server
```

Production build:

```powershell
D:\博士入学前\工具链\hugo-0.136.5\hugo.exe --gc --minify -b https://tianqin.netlify.app/
```

Go is required for Hugo modules and is kept outside the C drive:

```powershell
D:\博士入学前\工具链\go1.26.4\bin\go.exe version
```

## Public Content Boundary

Only public application-facing materials should be committed here:

- Website content
- Public CV PDF
- Publication and project summaries
- Selected English research notes

Do not commit transcripts, recommendation letters, application forms, private school lists, raw learning materials, or copyrighted books.

## Deployment

Netlify is the primary deployment target. The canonical site URL is:

https://tianqin.netlify.app/

GitHub Pages configuration may remain available as a secondary workflow, but Netlify is treated as the official public site.
