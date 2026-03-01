# אפליקציית תרגילי חשבון לכיתה ב'

אפליקציית משחק לימודית בעברית עם:
- חיבור וחיסור עד 100
- 20 שלבים עם התקדמות אוטומטית
- ממשק אינטראקטיבי לילדים
- הודעות הצלחה ושגיאה ידידותיות
- אפקטים קוליים מתחלפים

## הרצה מקומית

1. התקנת ספריות:

```bash
pip install -r requirements.txt
```

2. הרצת האפליקציה:

```bash
python -m streamlit run app.py
```

3. פתיחה בדפדפן:

`http://localhost:8501`

## פרסום דרך GitHub + Streamlit Cloud (מומלץ לכיתה)

> GitHub לבדו לא מריץ אפליקציית Python אינטראקטיבית. 
> לכן מפרסמים את הקוד ב-GitHub, ו-Streamlit Cloud מריץ אותו מה-Repo.

### שלב 1: העלאה ל-GitHub

בתיקיית הפרויקט הרץ:

```bash
git init
git add .
git commit -m "Initial commit - math app"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/<YOUR_REPO>.git
git push -u origin main
```

או, בצורה אוטומטית עם הסקריפט המצורף:

```powershell
.\publish_to_github.ps1 -GithubUser "YOUR_GITHUB_USER" -RepoName "YOUR_REPO"
```

### שלב 2: פריסה בענן (קישור ציבורי)

1. היכנס ל-Streamlit Community Cloud: `https://share.streamlit.io`
2. לחץ **New app**
3. בחר את ה-Repo שלך ב-GitHub
4. Main file path: `app.py`
5. לחץ **Deploy**

תקבל לינק קבוע בסגנון:
`https://<app-name>.streamlit.app`

### שלב 3: שיתוף בווטסאפ

שלח את הלינק שקיבלת, לדוגמה:

"ילדים, זה המשחק בחשבון שלנו 🎉\nכנסו מהטלפון/מחשב:\nhttps://<app-name>.streamlit.app"

## זמינות "תמיד חיה"

- ב-Streamlit Community Cloud החינמי, אפליקציה יכולה להירדם לאחר חוסר שימוש.
- אם צריך 24/7 ללא שינה, מומלץ שירות בתשלום (למשל Render / Railway / VPS).
