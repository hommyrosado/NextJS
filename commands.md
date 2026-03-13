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
