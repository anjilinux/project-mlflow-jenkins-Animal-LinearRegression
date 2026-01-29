pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/anjilinux/project-mlflow-jenkins-Animal-LinearRegression.git'
            }
        }

        stage('Setup Virtual Env') {
            steps {
                sh "pwd"
                sh '''
                python3 -m venv .venv
                . .venv/bin/activate
                pip install -r requirements.txt
                '''
                sh "pwd"
            }
        }

        stage('Train Model') {
            steps {
                sh "pwd"
                sh '''
                . .venv/bin/activate
                python train.py
                '''
                sh "pwd"
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
    // post {
    //     always {
    //         cleanWs()
    //     }
    // }





}
