pipeline {
    agent {
        node {
            dockerContainer {
                image 'devopsjourney1/myjenkinsagents:python'
                dockerHost 'unix:///var/run/docker.sock'
            }
            stage('Params') {
                if (env.BRANCH_NAME == 'main') {
                    echo 'I only execute on the master branch'
                } else {
                    echo 'I execute elsewhere'
                }
            }
        }
    }
    options {
        timeout(time: 1, unit: 'MINUTES') 
    }
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')
        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')

    }
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Params') {
            steps {
                echo "Printing params.."
                echo "Hello ${params.PERSON}"
                echo "Biography: ${params.BIOGRAPHY}"
                echo "Toggle: ${params.TOGGLE}"
                echo "Choice: ${params.CHOICE}"
                echo "Password: ${params.PASSWORD}"
            }
        }
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
                python3 app01/hello.py --name=Jhon
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
                script {
                    for (int i = 0; i < 10; ++i) {
                        echo "Contando ${i}"
                    }
                }
            }
        }
    }
    post { 
        always { 
            echo 'Post always message'
        }
        changed { 
            echo 'Post changed message'
        }
        fixed { 
            echo 'Post fixed message'
        }
        regression { 
            echo 'Post regression message'
        }
        aborted { 
            echo 'Post aborted message'
        }
        failure { 
            echo 'Post failure message'
        }
        success { 
            echo 'Post success message'
        }
        unstable { 
            echo 'Post unstable message'
        }
        unsuccessful { 
            echo 'Post unsuccessful message'
        }
        cleanup { 
            echo 'Post cleanup message'
        }
    }
}