pipeline {
   agent any
   stages {
       stage('Check Changes') {
           steps {
               script {
                   def changes = script: 'git diff --name-only ${env.BRANCH_NAME}^ ${env.BRANCH_NAME}', returnStatus: true
                   if (changes.contains('docs/')) {
                       echo 'Documentation changes detected. Skipping the job.'
                       currentBuild.result = 'SUCCESS'  // Set the result to SUCCESS or any other appropriate status
                       return
                   }
               }
           }
       }
       stage('Your Other Stages') {
           steps {
               sh "pwd"
           }
       }
   }
}