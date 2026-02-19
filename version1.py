pipeline {
    agent any
    stages {
        stage('Version 3: File Handling') {
            steps {
                checkout scm

                bat "echo Experiment 1 Version 3 Result > output.txt"
                bat "type output.txt"
            }
        }
    }
}