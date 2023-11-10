pipeline {
   agent any
   stages {
       stage("First Stage") {
           when {
                  // Check for changes before executing the stage
                      expression {
                      def excludedPath = 'docs'
                     // Check if any changes occurred in the excluded directory
                      def changesInDocs = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^${excludedPath}/'", returnStatus: true) == 0
                     // Skip the stage if changes occurred in the "docs" directory
                      return !changesInDocs
                               }
                }
           steps {
               echo "Executing the first stage."
           }
       }
       stage("Second Stage") {
           when {
                  // Check for changes before executing the stage
                      expression {
                      def excludedPath = 'docs'
                     // Check if any changes occurred in the excluded directory
                      def changesInDocs = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^${excludedPath}/'", returnStatus: true) == 0
                     // Skip the stage if changes occurred in the "docs" directory
                      return !changesInDocs
                               }
                }
           steps {
               echo "Executing the second stage."
           }
       }
       
   }
}
