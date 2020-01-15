pipeline {
    agent any
    environment {
        CC='golang'
        GITHUB_ACCESS_KEY_ID = credentials('github-id')
    }
    parmeters {
        string(name: 'Greting',defaultValue: 'hello',description: 'how should i greet the world')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building.. aaaaaaaaaaaaaaaaaaaa'
                echo "${params.Greting} world!"
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
                echo "${GITHUB_ACCESS_KEY_ID_USR}"
                echo "${GITHUB_ACCESS_KEY_ID_PSW}"
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
