pipeline {
    agent any


    script{
     def isDocsChange = {
        return !(sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0 && !(sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0))
    }
    }
    

    stages {
        stage("First Stage") {
            when { expression { isDocsChange() } }
            steps {
                echo "Executing the first stage."
            }
        }

        stage("Second Stage") {
            when { expression { isDocsChange() } }
            steps {
                echo "Executing the second stage."
            }
        }
    }
}
