1. Create environment: python3 -m venv venv; source venv/bin/activate 

2. Install apps: pip install -r requirements.txt 

3. Create .env file and add to it: ex: DATABASE_URL=postgresql://login:password@host/db (replace to yours credentials)

3. Start application: uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
