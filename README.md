# Children's Health Monitoring System

A Streamlit-based web application for monitoring children's growth patterns and comparing them with WHO standards.

## Features

- Real-time data visualization of children's growth metrics
- Comparison with WHO growth standards
- Separate analysis for boys and girls
- Interactive test portal for data entry
- Growth charts for height, weight, and BMI
- Firebase integration for data storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gnanendranaidun/Crescere-data.git
cd Crescere-data
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Local Development

Run the application locally:
```bash
streamlit run vis1.py
```

The application will be available at http://localhost:8501

## Deployment Options

### 1. Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app by selecting the repository

### 2. Heroku

1. Create a `Procfile`:
```
web: streamlit run vis1.py
```

2. Deploy using Heroku CLI:
```bash
heroku create your-app-name
git push heroku main
```

### 3. Docker

1. Build the Docker image:
```bash
docker build -t health-monitoring-app .
```

2. Run the container:
```bash
docker run -p 8501:8501 health-monitoring-app
```

## Environment Variables

Configure the following environment variables:
- `FIREBASE_URL`: Your Firebase database URL

## Data Security

- The application uses Firebase Realtime Database
- Ensure proper security rules are set in Firebase Console
- Use environment variables for sensitive information
- Implement authentication if needed

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
