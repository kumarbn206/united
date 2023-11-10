pipeline {
   agent any
   stages {
       stage("First Stage") {
           when {
               expression {
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   def allChanges = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()
                   return !(docsChanges || allChanges)
               }
           }
           steps {
               echo "Executing the first stage."
           }
       }
       stage("Second Stage") {
           when {
               expression {
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   def allChanges = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()
                   return !(docsChanges || allChanges)
               }
           }
           steps {
               echo "Executing the second stage."
           }
       }
   }
}