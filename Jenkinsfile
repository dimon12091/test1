// pipeline {
//     environment {
//         registryCredential = 'dockerhub'
//         app = ''
//     }
//     agent any
//     stages {
//       stage("SCM") {
//         steps {
//             checkout([
//               $class: 'GitSCM',
//               branches: [[name: 'master']],
//               userRemoteConfigs: [[credentialsId: 'github-ssh-key', url: 'git@github.com:dimon12091/test1.git']]
//             ])
//         }
//       }
//       stage('Build') {
//         steps{
//             scripts{
//                 app = docker.build("wolfmoon69/test1")
//             }
//         }
//       }
//       stage('Test image') {
//          app.inside {
//             sh 'echo "Tests passed"'
//          }
//       }
//       stage('Push image') {
//         docker.withRegistry('https://registry.hub.docker.com', 'git') {
//         app.push("${env.BUILD_NUMBER}")
//         app.push("latest")
//         }
//       }
//     }
// }
pipeline {
    environment {
    registry = "wolfmoon69/test1"
    registryCredential = 'dockerhub'
    app = ''
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
    stage('Building image') {
      steps{
        script {
        sh 'sudo usermod -aG docker $USER'
        sh 'groups'
          app = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  }
}

