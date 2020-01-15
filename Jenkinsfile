pipeline {
    agent any
    environment {
        CC='golang'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building.. aaaaaaaaaaaaaaaaaaaa'
            }
        }
        stage('Test') {
            environment {
                CB='Python'
            }
            steps {
                echo 'Testing.. bbbbbbbbbbbbbbb'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                echo "${CC}"
                echo "${CB}"
                sh 'printenv'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.... ccccccccccccccc'
            }
        }
    }
}
