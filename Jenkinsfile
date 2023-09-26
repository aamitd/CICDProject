pipeline {
    agent {
        kubernetes {
            label 'amitapp'
            yamlFile 'build-pod.yaml'
            defaultContainer 'amitapp-docker-helm-build'
        }
    }

    environment {
        DOCKER_REGISTRY = 'https://registry.hub.docker.com'
        DOCKER_HUB_CREDENTIALS = credentials('DockerHubb') 
    }

    stages {
        stage('Test Docker') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo 'Starting Docker build...'
                        // Build the Docker image from the current directory
                        def dockerImage = docker.build('aamitd/amitrepo:latest', '.')
                        echo 'Docker build completed.'
                    } catch (Exception e) {
                        // Print detailed error information
                        echo "Error: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        error("Docker build failed")
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo 'Running Pytest...'
                    sh 'docker run aamitd/amitrepo:latest pytest testapp.py'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Starting Docker push...'

                    // Log in to Docker Hub using credentials
                    withCredentials([usernamePassword(credentialsId: 'DockerHubb', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push aamitd/amitrepo:latest
                        '''
                    }

                    echo 'Docker push completed.'
                }
            }
        }

        stage('Email Notification') {
            steps {
                script {
                mail(body: "${JOB_NAME}, build ${BUILD_NUMBER} Pytest completed.", subject: 'Pytest completed.', to: 'aamit.dahan@gmail.com')                }
            }
        }
    }

    post {
        success {
            echo 'Docker image pushed successfully.'
        }
    }
}
