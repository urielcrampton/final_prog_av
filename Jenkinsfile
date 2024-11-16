pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/urielcrampton/final_prog_av'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("nombre_imagen_docker:${env.BUILD_ID}")
                    // Usa 'bat' para ejecutar comandos en Windows
                    bat 'docker build -t nombre_imagen_docker:${env.BUILD_ID} .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover tests'
                    }
                }
            }
        }
        stage('Package') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python setup.py sdist'
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/dist/*.tar.gz', allowEmptyArchive: true
        }
        success {
            emailext subject: "Pipeline Éxitoso: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                     body: "El pipeline ha sido ejecutado con éxito.\nJob: ${env.JOB_NAME}\nBuild: ${env.BUILD_NUMBER}\nVer detalles: ${env.BUILD_URL}",
                     to: 'uricrampton@gmail.com'
        }
        failure {
            emailext subject: "Pipeline Fallido: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                     body: "El pipeline ha fallado.\nJob: ${env.JOB_NAME}\nBuild: ${env.BUILD_NUMBER}\nVer detalles: ${env.BUILD_URL}",
                     to: 'uricrampton@gmail.com'
        }
    }
}
