Site: https://youtu.be/6sfiAyKy8Jo?si=LcbBSNzdR7XE0G1q

tree -I ".venv"
pip freeze > requirements.txt

pip install requests beautifulsoup4
pip install pandas requests beautifulsoup4 python-dotenv

pip install fastapi uvicorn

pip freeze > requirements.txt

uvicorn youtube_intelligence.api.main:app --reload
or
uvicorn api.main:app --reload

For codespaces:
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

Check for ports:
lsof -i :8000

Example:
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
uvicorn 23633 codespace 3u IPv4 1051467 0t0 TCP localhost:8000 (LISTEN)

kill -9 23633

find . -type d -name "**pycache**" -exec rm -r {} +
find . -type f -name "\*.pyc" -delete

USING FASTAPI:
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

CURL:
curl http://127.0.0.1:8000/collect
GIT:
git switch -c dev
git push -u origin dev

1️⃣ Switch to your base branch first

Most teams branch features from dev.

git switch dev
git pull
2️⃣ Create the feature branch
git switch -c feature/my-new-feature

Example:

git switch -c feature/youtube-dashboard

This will:

create the branch

switch to it

3️⃣ Push the feature branch to remote
git push -u origin feature/youtube-dashboard
4️⃣ Check your branches
git branch

Example output:

main
dev
* feature/youtube-dashboard
🧠 Common naming conventions
feature/youtube-dashboard
feature/api-refactor
feature/channel-comparison
bugfix/csv-export
hotfix/login-error



