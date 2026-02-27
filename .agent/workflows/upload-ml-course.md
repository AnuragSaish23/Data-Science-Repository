---
description: Upload ML/DL course work to GitHub repository
---

# Upload ML/DL Course Work

This workflow uploads your Machine Learning and Deep Learning course work to GitHub.

## Prerequisites
- Working directory: `c:\Users\druma\Desktop\Machine and Deep Learning`
- Git repository already initialized and connected to remote

## Steps

1. Navigate to the repository folder
// turbo
```bash
cd "c:\Users\druma\Desktop\Machine and Deep Learning"
```

2. Check what files have been changed
// turbo
```bash
git status
```

3. Stage all changes (new notebooks, modified files)
```bash
git add .
```

4. Create a meaningful commit message with today's date and module name
```bash
git commit -m "📚 [Module-Name] Add content - YYYY-MM-DD"
```
> Replace `[Module-Name]` with the actual module (e.g., Advanced-Python, Machine-Learning)
> Replace `YYYY-MM-DD` with current date

5. Push to GitHub
```bash
git push origin main
```

6. Update README if needed
- Update the progress table in README.md
- Change module status from ⏳ to 🔄 or ✅ as appropriate

## Notes
- The assistant will help update the README progress tracker automatically
- Commit messages follow format: `📚 [Module-Name] Add content description`
