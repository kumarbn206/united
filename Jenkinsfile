pipeline {

    agent any

    stages {

        stage('Replace Text in XML') {

            steps {

                script {

                    def branchName = env.BRANCH_NAME // Get the current branch name

                    def xmlFilePath = 'default.xml'

                    // Read the existing XML content

                    def xmlContent = readFile(xmlFilePath)

                    // Replace the desired text

                    def updatedXmlContent = xmlContent.replaceAll(

                        '<project name="tef83xx/boot" path="origin/boot" groups="default">',

                        '<project name="tef83xx/boot" path="origin/boot" groups="default" revision="' + branchName + '">'

                    )

                    // Write the updated content back to the file

                    writeFile file: xmlFilePath, text: updatedXmlContent

                }

            }

        }

    }

}
