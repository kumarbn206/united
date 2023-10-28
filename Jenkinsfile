pipeline {
    agent any
    stages {
        stage("changes in the folder") {
            steps {
                sh """
                echo "kumar"
                echo "BN"
                """
            }
        }
    }


    stage("Checkout") {
            steps {
                script {
                    def changes = checkout changelog: true, poll: false
                    if (changes.any { it.path.startsWith('docs/') }) {
                        currentBuild.result = 'ABORTED'
                        error('Aborted due to changes in the "docs" folder.')
                    }
                }
            }

            
}
