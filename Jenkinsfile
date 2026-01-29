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
    
    stage('Deploy & Test Flask') {
        steps {
            sh '''
            set -e

            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%%Activating virtual environment...#########@@@$$$$$$$$$$$$$$$"
            . .venv/bin/activate

            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%% Starting Flask app in background...#################@@@@@@@@@@@@@@@@@%%%%%%%%A"
            nohup python app.py > flask.log 2>&1 &
            FLASK_PID=$!
            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%% Flask PID: $FLASK_PID #################@@@@@@@@@@@@@@@@@%%%%%%%%A"

            sleep 5

            if ! ps -p $FLASK_PID > /dev/null; then
                echo "Flask crashed. Logs:"
                cat flask.log
                exit 1
            fi

            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%% Health check...  #################@@@@@@@@@@@@@@@@@%%%%%%%%"
            curl -f http://127.0.0.1:5001/health

            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%%A   Prediction test..."#################@@@@@@@@@@@@@@@@@%%%%%%%%A 
            curl -f -X POST http://127.0.0.1:5001/predict \
                -H "Content-Type: application/json" \
                -d '{"features":[120,22.5,1100,0.78]}'

            echo "#################@@@@@@@@@@@@@@@@@%%%%%%%%A Keeping app alive for 2 minutes... #################@@@@@@@@@@@@@@@@@%%%%%%%%A"
            sleep 10

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
