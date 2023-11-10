def excludedPath = 'docs'
def changesInDocs = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^${excludedPath}/'", returnStatus: true) == 0
if (changesInDocs) {
   echo "Changes detected in 'docs'. Skipping subsequent stages."
} else {
   pipeline {
       agent any
       stages {
           stage("First Stage") {
               steps {
                   // Your steps for the first stage
                   echo "Executing the first stage."
               }
           }
           stage("Second Stage") {
               steps {
                   // Your steps for the second stage
                   echo "Executing the second stage."
               }
           }
           // Add more stages as needed
       }
   }
}