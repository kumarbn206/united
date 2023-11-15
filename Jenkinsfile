pipeline {
   agent any
   stages {
       stage('Check Changes') {
           steps {
               script {
                   def docsChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -E '^docs/'", returnStatus: true) == 0
                    def otherChanges = sh(script: "git diff --name-only HEAD^ HEAD | grep -Ev '^docs/'", returnStatus: true) == 0
                    return !(docsChanges && !otherChanges)
                       currentBuild.result = 'SUCCESS'
                       error('Aborting further stages.')
                       
                   }
               }
           }
       }
       stage('Your Other Stages') {
           steps {
               echo 'This stage will only run if there are no documentation changes.'
               // Your other stage steps here
           }
       }
   }
}