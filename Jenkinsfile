pipeline {
    agent { 
        node {
            label 'python-docker'
            }
      }
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 120, unit: 'SECONDS')
    }
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    triggers { pollSCM('H/10 * * * *') }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                pip3 install -r app01/requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
                echo "Hello ${params.PERSON}"
                python3 app01/hello.py --name ${params.PERSON}
                python3 app01/hello.py --name=Jhon}
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}