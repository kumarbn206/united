pipeline {
   agent any
   stages {
       stage('Check Changes') {
           steps {
               script {
                   def changes = sh(script: 'git diff --name-only ${env.BRANCH_NAME}^ ${env.BRANCH_NAME}', returnStdout: true).trim()
                   if (changes.contains('docs/')) {
                       echo 'Documentation changes detected. Skipping the job.'
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