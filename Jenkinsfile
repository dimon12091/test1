pipeline {
    environment {
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
      stage("SCM") {
        steps {
            checkout([
              $class: 'GitSCM',
              branches: [[name: 'master']],
              userRemoteConfigs: [[credentialsId: 'github-ssh-key', url: 'git@github.com:dimon12091/test1.git']]
            ])
            }
        }

      stage('Fire Up docker-compose') {
        steps {
            sh "docker-compose build"
//             step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
//                 sh 'docker-compose up -d volume && sleep 5'
//                 sh 'docker-compose up -d config-seed && sleep 60'
//                 sh 'docker-compose up -d mongo && sleep 10'
//                 sh 'docker-compose up -d logging && sleep 60'
//                 sh 'docker-compose up -d notifications && sleep 30'
//                 sh 'docker-compose up -d metadata && sleep 60'
//                 sh 'docker-compose up -d data && sleep 60'
//                 sh 'docker-compose up -d command && sleep 60'
//                 sh 'docker-compose up -d scheduler && sleep 60'
//                 sh 'docker-compose up -d export-client && sleep 60'
//                 sh 'docker-compose up -d export-distro && sleep 60'
//                 sh 'docker-compose up -d rulesengine && sleep 60'
//                 sh 'docker-compose up -d device-virtual && sleep 60'

        }
      }
    }
}
