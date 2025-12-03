pipeline {
    agent any

    environment{
        DOCKER_IMAGE_NAME="karan9270/python-test-app"

        DOCKER_USER_NAME="karan9270"

        DOCKER_AUTH_TOKEN=credentials('DOCKER_AUTH_TOKEN')

    }
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

        stage('prepare the docker image') {
            steps {
                sh 'docker image build -t ${DOCKER_IMAGE_NAME} .'
                echo "hell"
            }
        }
        stage('docker login') {
            steps {
                sh 'echo ${DOCKER_AUTH_TOKEN} | docker login -u ${DOCKER_USER_NAME} --password-stdin'
            }
        }
        stage('push docker image') {
            steps{
            sh 'docker image push ${DOCKER_IMAGE_PUSH}'
            }
        }
        stage('restart service') {
            steps{
                sh 'docker service update --force --image ${DOCKER_IMAGE_NAME} python-app'
            }
        }
    }
}