pipeline {
    agent any

    environment {
        // Define your Docker image name
        IMAGE_NAME = "hello-world-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the repository from your source control system
                git url: 'https://your-repo-url.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with a tag that includes the build number
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                script {
                    // Run the Docker container in detached mode mapping port 5000
                    dockerContainer = dockerImage.run("-d -p 5000:5000")
                    echo "Container started with ID: ${dockerContainer.id}"
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
