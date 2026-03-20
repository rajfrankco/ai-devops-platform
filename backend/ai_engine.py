import requests

def analyze_logs(logs):
    try:
        response = requests.post(
            "http://ollama:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"""
                Analyze DevOps logs.
                Give:
                - Root cause
                - Fix
                - Severity

                Logs:
                {logs}
                """,
                "stream": False
            }
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}