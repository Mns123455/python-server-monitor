pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-server-monitor .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f python-server-monitor-container || true
                    docker run -d \
                      --restart unless-stopped \
                      -p 5001:5000 \
                      --name python-server-monitor-container \
                      python-server-monitor
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'curl -fsS http://localhost:5001/health'
            }
        }
    }
}
