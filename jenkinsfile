pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourrepo/forest-animal-mlops.git'
            }
        }

        stage('Setup Virtual Env') {
            steps {
                sh '''
                python3 -m venv .venv
                . .venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . .venv/bin/activate
                python train.py
                '''
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '''
                . .venv/bin/activate
                python evaluate.py
                '''
            }
        }

        stage('Test Model') {
            steps {
                sh '''
                . .venv/bin/activate
                pytest test_model.py
                '''
            }
        }
    }
}
