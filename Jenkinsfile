pipeline {

    agent any

    stages {

        stage("First Stage") {

       when { expression { return !(sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0 && !(sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0)) } }


            steps {

                echo "Executing the first stage."

            }

        }

        stage("Second Stage") {

         when { expression { return !(sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0 && !(sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0)) } }


            steps {

                echo "Executing the second stage."

            }

        }

    }

}