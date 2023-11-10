pipeline {
   agent any
   stages {
       stage("Check for Changes in the docs") {
           steps {
               script {
                   def excludedPath = 'docs'
                   def changesInDocs = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^${excludedPath}/'", returnStatus: true) == 0
                   if (changesInDocs) {
                       echo "Changes detected in 'docs'. Skipping subsequent stages."
                   } else {
                       buildStages()
                   }
               }
           }
       }
   }
}
def buildStages() {
   stage("First Stage") {
       steps {
           sh """
              echo "hellog"
           """
       }
   }
   stage("second Stage") {
       steps {
           sh """
              echo "hellog"
           """
       }
   }


   stage("third Stage") {
       steps {
           sh """
              echo "hellog"
           """
       }
   }

}