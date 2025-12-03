pipeline {
    agent any

    //environment{}
    stages {
        stage('scm') {
            steps {
                echo "taken care by jenkins"
            }
        }
        stage('prepare env') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
            
        }
        stage('test the app') {
            steps {
                sh 'python3 -m pytest test_app.py'
            }
        }

        stage('prepare the image') {
            steps {
                echo "hell"
            }
        }
    }
}