pipeline {
   agent any
   stages {
       stage("First Stage") {
           when {
               expression {
                   def allChanges = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   return docsChanges && allChanges.split('\n').size() == 1
               }
           }
           steps {
               echo "Executing the first stage."
           }
       }
       stage("Second Stage") {
           when {
               expression {
                   def allChanges = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   return docsChanges && allChanges.split('\n').size() == 1
               }
           }
           steps {
               echo "Executing the second stage."
           }
       }
       
   }
}
