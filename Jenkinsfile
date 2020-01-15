pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.. aaaaaaaaaaaaaaaaaaaa'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing.. bbbbbbbbbbbbbbb'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.... ccccccccccccccc'
            }
        }
    }
}
