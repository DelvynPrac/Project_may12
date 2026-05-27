pipeline {
    agent any

    stages { 

        /*stage('git checkout') {
           steps {
                git 'https://github.com/DelvynPrac/Project_may12.git'
                // git '   
                }
        } */

        stage('build') {
            steps {
                sh 'docker build -t project_may12 .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop project_may12_container || true
                docker rm project_may12_container || true
                docker run -d -p 8000:4500 --name project_may12_container project_may12
                '''
            }
        }

        stage('Wait for Container') {
            steps {
                sh 'sleep 7'
            }
        }

        stage('Test') {
            steps {
                sh """
                curl -X POST http://localhost:8000/ask \
                -H "Content-Type: application/json" \
                -d '{"question":"What is the capital of France?"}'
                """
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                docker stop project_may12_container || true
                docker rm project_may12_container || true
                '''
            }
        }
    }
}




