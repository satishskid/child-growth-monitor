FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 8501

# Command to run the application
ENTRYPOINT ["streamlit", "run", "vis1.py", "--server.port=8501", "--server.address=0.0.0.0"]
