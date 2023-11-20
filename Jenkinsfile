pipeline {
    agent any

    stages {
        stage('get build number'){
            steps{
                script{
                   def jobName = 'united/main'  // Replace 'YourJobName' with the actual name of the Jenkins job
def jenkins = Jenkins.getInstance()
def job = jenkins.getItemByFullName(jobName, Job.class)
def lastBuild = job.getLastBuild()
if (lastBuild) {
   def buildNumber = lastBuild.number
   println "Latest build number for job '${jobName}': ${buildNumber}"
} else {
   println "No builds found for job '${jobName}'"
}
                }
            }
        }
    }
}



