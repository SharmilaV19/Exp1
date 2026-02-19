pipeline {
    agent any
    parameters {
        string(name: 'MESSAGE', defaultValue: 'Version 2 active', description: 'Parameter verification')
    }
    stages {
        stage('Version 2: System Date') {
            steps {
                checkout scm
                bat "date /t"
                
                echo "The parameter value is: ${params.MESSAGE}"
            }
        }
    }
}