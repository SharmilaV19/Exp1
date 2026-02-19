pipeline {
    agent any
    parameters {
        // Task 2: Accept VERSION parameter
        string(name: 'VERSION', defaultValue: '1.0', description: 'Enter Build Version')
    }
    stages {
        stage('Version 3') {
            steps {
                checkout scm
                // Task 3: Create version.txt
                bat "echo ${params.VERSION} > version.txt"
                bat "type version.txt"
            }
        }
    }
}