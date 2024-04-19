// Basic Pipeline for building the docker containers 

pipeline {
    agent any

    stages {
        stage('check out') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Commu-net/Communet-Api'
            }
        }
        
        stage('code analysis'){
            steps{
                echo "code analysis"
            }
        }
        
        stage('get env'){
            steps{
                sh 'cp /home/ubuntu/.env .'
            }
        }
        
        stage("building"){
            steps{
                sh 'docker compose up --build -d'
                echo 'compose up'
            }
        }
    }
}
