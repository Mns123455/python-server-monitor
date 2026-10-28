pipeline {
    agent any

    stages {
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

        stage('Wait and Test') {
            steps {
                sh '''
                    sleep 5
                    docker ps -a
                    docker logs --tail 30 python-server-monitor-container
                    curl --retry 10 --retry-connrefused --retry-delay 2 \
                      --max-time 5 -fsS http://localhost:5001/health
                '''
            }
        }
    }
}
