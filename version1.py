pipeline {
    agent any
    stages {
        stage('Version 4') {
            steps {
                checkout scm
                // Task 2: Print Git Commit ID
                echo "The Git Commit ID is: ${env.GIT_COMMIT}"
                
                // Task 3: Final build result
                echo "Build Version 4 is Complete!"
            }
        }
    }
}