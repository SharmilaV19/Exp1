pipeline {
    agent any
    parameters {
        string(name: 'USERNAME', defaultValue: 'Sharmila', description: 'Enter the username to store')
    }
    stages {
        stage('Version 4: User Logging') {
            steps {
                checkout scm
                echo "Username has been successfully saved to user.txt"
                
                bat "type user.txt"
            }
        }
    }
}