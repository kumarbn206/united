pipeline {
    agent any

    stages {
        stage("Check Docs Changes") {
            steps {
                script {
                    def isDocsChange = {
                        return !(sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0 && !(sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0))
                    }
                    env.IS_DOCS_CHANGE = isDocsChange() ? 'true' : 'false'
                }
            }
        }

        stage("First Stage") {
            when { expression { env.IS_DOCS_CHANGE == 'true' } }
            steps {
                echo "Executing the first stage."
            }
        }

        stage("Second Stage") {
            when { expression { env.IS_DOCS_CHANGE == 'true' } }
            steps {
                echo "Executing the second stage."
            }
        }
    }
}
