# פריסה מיידית ל-GitHub ולינק ציבורי

## 1) יצירת Repo ריק ב-GitHub
1. היכנס ל-https://github.com/new
2. Repository name: למשל `math-class-b`
3. בחר Public
4. לחץ Create repository

## 2) הרצת סקריפט ההעלאה (PowerShell)
בתיקיית הפרויקט הרץ:

```powershell
.\publish_to_github.ps1 -GithubUser "YOUR_GITHUB_USER" -RepoName "math-class-b"
```

> בהרצה הראשונה GitHub יבקש התחברות (או token) לצורך push.

## 3) פריסה ב-Streamlit Cloud
1. היכנס ל-https://share.streamlit.io
2. לחץ New app
3. בחר את ה-repo שיצרת
4. Main file path: `app.py`
5. לחץ Deploy

## 4) שיתוף בווטסאפ
שלח את הלינק שקיבלת (בסגנון `https://xxxx.streamlit.app`) לכל הכיתה.
