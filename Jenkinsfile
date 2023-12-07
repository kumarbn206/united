pipeline {
    agent any

    stages {
      
      stage("Upstream job")
      {
        steps{
            sh"""
            echo "hello"                    
            def upstreamBuildNumber = env.UPSTREAM_BUILD_NUMBER
            echo "Upstream Build Number in Downstream Job: ${upstreamBuildNumber}"
            """
        }
      }
    }
}
