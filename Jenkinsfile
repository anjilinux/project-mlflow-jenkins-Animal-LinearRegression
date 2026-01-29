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
        // stage("deploy on flask-api"){
        //     steps{
        //         sh '''
        //         . .venv/bin/activate
        //         python app.py

        //         '''
        //     }
        // }
    
        stage('Run Flask App (2 minutes)') {
            steps {
                sh '''
                echo "Starting Flask app in background..."

                # Activate virtualenv if needed
                . .venv/bin/activate

                # Run Flask in background
                nohup python app.py > flask.log 2>&1 &

                
                #curl http://127.0.0.1:5001/health

                # Save PID
                echo $! > flask.pid

                echo "Flask PID: $(cat flask.pid)"

                # Wait for 2 minutes
                sleep 120

                echo "Stopping Flask app..."
                kill $(cat flask.pid) || true
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
