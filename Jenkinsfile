pipeline {
    agent any

    stages {
        stage("Testing") {
            steps {
              sh"""
                echo "hello"
              """
            }
        }

    

        stage('Upstream') {
            steps {
                // Your upstream job steps here

                // Trigger downstream job
                build job: 'Downstream', wait: false
            }
        }
    }
}
