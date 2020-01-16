pipeline {
    agent any
    environment {
        CC='golang'
        GITHUB_ACCESS_KEY_ID = credentials('github-id')
    }
    parameters {
        string(name: 'Greting',defaultValue: 'hello',description: 'how should i greet the world')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building.. aaaaaaaaaaaaaaaaaaaa'
				echo 'from dev branch'
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
    post {
        success {
            dingTalk accessToken: 'https://oapi.dingtalk.com/robot/send?access_token=4cc67d02e646aa52fbdaef4942bf379ca5317adede42a61c26a7c7877c890f39', imageUrl: '', jenkinsUrl: '', message: 'devops test', notifyPeople: ''
        }
    }
}
