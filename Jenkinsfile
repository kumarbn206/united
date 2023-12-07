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
                script {
                    // Convert build number to string and trigger downstream job with build number parameter
                    def downstreamBuild = build job: 'downstream', parameters: [string(name: 'UPSTREAM_BUILD_NUMBER', value: currentBuild.number.toString())], wait: false
                   
                }
            }
        }
    }
}
