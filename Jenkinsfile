pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "your-dockerhub-username/travel-mlops"
        DOCKER_TAG = "latest"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test & Lint') {
            steps {
                echo 'Running unit tests and syntax checks...'
                // You could add: sh 'pytest tests/' or 'flake8 .'
                sh 'python -m py_compile app.py streamlit_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image for Flask API & Streamlit...'
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Push to Registry') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes Cluster...'
                // Ensure kubeconfig is configured properly in Jenkins
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl apply -f kubernetes/service.yaml'
                
                // Force rollout to pull the latest image
                sh 'kubectl rollout restart deployment/travel-mlops-flask'
                sh 'kubectl rollout restart deployment/travel-mlops-streamlit'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline successfully executed. The models are deployed!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}
