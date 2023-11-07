pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
           echo "Hello"
            }
        }

        stage("changes in the folder") {
            steps {
                sh """
                echo "kumar"
                """
            }
        }

       stage('Checkout') {
            steps {
                script {
                    // Define the excluded directory "docs"
                    def excludedPath = 'docs'

                    // Perform the default Git checkout
                    

                    // Enable sparse-checkout and exclude the "docs" directory
                    sh "git config core.sparseCheckout true"
                    sh "echo ${excludedPath} >> .git/info/sparse-checkout"
                    sh "git read-tree -mu HEAD"
                }
            }
        }


    }
}
