# sql-llm-app

A Streamlit-based application that converts natural language queries into SQL using Groq's LLM and executes them against a Neon PostgreSQL database.

## Prerequisites
- Python 3.10+
- Docker
- GitHub account (for cloud deployment)
- EuriAI API key
- Neon database account

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/pavanbairu/sql-llm-app.git
   cd sql-llm-app
   ```

2. **Set up environment variables**:
   Create a `.env` file in the `app/` directory:
   ```bash
   EURIAI_API_KEY=<your-euriai-api-key>
   DATABASE_URI=postgresql://neondb_owner:<your-neon-password>@ep-cool-mode-a4i17css-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require
   ```

3. **Install dependencies**:
   ```bash
   cd app
   pip install -r requirements.txt
   ```

4. **Run locally (without Docker)**:
   ```bash
   streamlit run main.py
   ```

5. **Build and run with Docker**:
   ```bash
   cd ..
   docker build -t sql-llm-app .
   docker run -p 8501:8501 --env-file .env sql-llm-app
   ```

6. **Test the app**:
   - Open `http://localhost:8501` in your browser.
   - Enter a natural language query (e.g., "Show all users from the database").
   - Verify the SQL query is generated and executed against the Neon database.