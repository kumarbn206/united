pipeline {
   agent any
   stages {
       stage('Update XML') {
                             steps {
                                script {
                                def branchName = env.BRANCH_NAME // Get the current branch name
                                def xmlFilePath = 'default.xml'
                                if (branchName != 'develop' && branchName != 'release') {
                                
                                // Read the existing XML content
                                def xmlContent = readFile(xmlFilePath)
                                // Replace text
                              //   def updatedXmlContent = xmlContent.replaceAll('<project name="tef83xx/boot" path="origin/boot" groups="default">','<project name="tef83xx/boot" path="origin/boot" groups="default" revision="' + branchName + '">' )
                              def updatedXmlContent = xmlContent.replaceAll('<project name="tef83xx/boot"', '<project name="tef83xx/boot" revision="' + branchName + '"')
                                   
                               // Write the updated content back to the file
                               writeFile file: xmlFilePath, text: updatedXmlContent
                                 }

                                       }
                                   }

           }
   }
}