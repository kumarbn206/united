pipeline {
    agent any

    stages {
        stage("Check Docs Changes") {
            steps {
              sh"""
                echo "hello"
              """
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
