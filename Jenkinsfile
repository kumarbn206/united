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
                    // Trigger downstream job with build number parameter
                    def downstreamBuild = build job: 'downstream', parameters: [string(name: 'UPSTREAM_BUILD_NUMBER', value: currentBuild.number)], wait: false
                    echo "Triggered Downstream Job: ${downstreamBuild.url}"
                }
            }
        }
    }
}
