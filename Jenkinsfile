pipeline {
    agent any

    stages {
        stage('get build number'){
            steps{
                script{
                 def buildNumber = Jenkins.instance.getItem('united/main').getItem('main').lastSuccessfulBuild.number
                 sh """
                 echo ${buildNumber}
                 """
                }
            }
        }
    }
}