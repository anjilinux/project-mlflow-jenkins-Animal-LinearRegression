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
    
       stage('Deploy & Test Flask') {
            steps {
                sh '''
                set -e

                echo "Starting Flask app in background..."
                nohup python app.py > flask.log 2>&1 &
                FLASK_PID=$!
                echo "Flask PID: $FLASK_PID"

                # Wait for Flask to bind
                sleep 10

                # Check if Flask is still running
                if ! ps -p $FLASK_PID > /dev/null; then
                    echo "Flask crashed. Logs:"
                    cat flask.log
                    exit 1
                fi

                echo "Health check..."
                curl -f http://127.0.0.1:5001/health

                echo "Prediction test..."
                curl -f -X POST http://127.0.0.1:5001/predict \
                    -H "Content-Type: application/json" \
                    -d '{"features":[120,22.5,1100,0.78]}'

                echo "Keeping app alive for 2 minutes..."
                sleep 120

                echo "Stopping Flask..."
                kill $FLASK_PID
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
