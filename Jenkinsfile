pipeline {
    agent any


    stage("Check for Changes") {
            steps {
                script {
                    // Define the excluded directory "docs"
                    def excludedPath = 'docs'
                    
                    // Check if any changes occurred in the excluded directory
                    def changesInDocs = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^${excludedPath}/'", returnStatus: true) == 0

                    // Abort the build if changes occurred in the "docs" directory
                    if (changesInDocs) {
                        currentBuild.result = 'ABORTED'
                        error("Build aborted due to changes in the 'docs' directory.")
                    }
                }
            }
        }

    stages {
        stage("Checkout") {
            steps {
                echo "Hello"
                checkout scm
            }
        }

        stage("changes in the folder") {
            steps {
                sh """
                echo "kumar"
                """
            }
        }

  
    }
}
