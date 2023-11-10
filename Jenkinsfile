pipeline {
   agent any
   stages {
       stage("First Stage") {
           when {
               expression {
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   def otherChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0
                   return !docsChanges && otherChanges
               }
           }
           steps {
               echo "Executing the first stage."
           }
       }
       stage("second Stage") {
           when {
               expression {
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                   def otherChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0
                   return !docsChanges && otherChanges
               }
           }
           steps {
               echo "Executing the second stage."
           }
       }

   }

}


















pipeline {
   agent any
   stages {
       stage("First Stage") {
                  when {
                          expression {
                                     def allChanges = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()
                                     def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                                    return !(docsChanges && allChanges)
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
                                    return !(docsChanges && allChanges)
                                     }
                        }
           steps {
               echo "Executing the second stage."
           }
       }
       
   }
}
