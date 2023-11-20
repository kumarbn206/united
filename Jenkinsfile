pipeline {
    agent any

    stages {
        stage('get build number'){
            steps{
                script{
                    def jobName = 'united/main'  // Replace 'YourJobName' with the actual name of the Jenkins job
// Trigger the other Jenkins job and wait for its completion
def triggeredJob = build(jobName)
// Retrieve the build number of the triggered job
def buildNumber = triggeredJob.number
println "Latest build number for job '${jobName}': ${buildNumber}"
// Now you can use 'buildNumber' in your Jenkins pipeline
                }
            }
        }
    }
}