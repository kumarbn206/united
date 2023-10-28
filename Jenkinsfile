pipeline 
{
    agent any
    when {
          not {
              changeset 'docs/**'
          }
    }
    stages{
       stage("changes in the folder"){
        steps{
            sh """
             echo "kumar"
             echo "BN"
            """
        }
       }
    }
}