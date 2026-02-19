pipeline {
    agent any
    
    parameters {
        // This creates the input box in Jenkins
        string(name: 'USERNAME', defaultValue: 'Admin', description: 'Enter your name to save to a file')
    }
    
    stages {
        stage('Task 1: Checkout') {
            steps {
                // Pulls your latest code from GitHub
                checkout scm
            }
        }
        
        stage('Task 2 & 3: File Operations') {
            steps {
                // Writes the parameter value into a file called user.txt
                bat "echo ${params.USERNAME} > user.txt"
                
                echo "Success: Username has been saved."
                
                // Reads the file back to the console to prove it worked
                bat "type user.txt"
            }
        }
    }
}