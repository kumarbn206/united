pipeline {
    agent any

    stages {
        stage('get build number'){
            steps{
                script{
                 def jobName = 'united/main'  // Replace 'YourJobName' with the actual name of the Jenkins job
                  def jenkinsUrl = 'http://3.82.210.33:8080/'  // Replace 'http://your-jenkins-server-url/' with the URL of your Jenkins server
// Make an HTTP request to get information about the latest build
def response = httpRequest(
   url: "${jenkinsUrl}job/${jobName}/lastBuild/api/json",
   httpMode: 'GET',
   contentType: 'APPLICATION_JSON'
)
// // Parse the JSON response to extract the build number
// def buildNumber = readJSON text: response.content
// println "Latest build number for job '${jobName}': ${buildNumber.number}"
// You can now use 'buildNumber.number' in your Jenkins pipeline
                }
            }
        }
    }
}