pipeline {
    agent any
    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello from VS Code', description: 'Enter a message')
    }
    stages {
        stage('Task 1: Checkout') {
            steps {
                checkout scm 
            }
        }
        stage('Task 2 & 3: Console Output') {
            steps {
                echo "The parameter value is: ${params.MESSAGE}"
                bat "echo Hello from Jenkins"
            }
        }
    }
}

