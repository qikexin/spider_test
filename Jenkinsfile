pipeline {
    agent any
    environment {
        CC='golang'
        GITHUB_ACCESS_KEY_ID = credentials('github-id')
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
                echo "${GITHUB_ACCESS_KEY_ID}"
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
