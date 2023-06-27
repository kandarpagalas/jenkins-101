pipeline {
    agent {
        dockerContainer {
            image 'devopsjourney1/myjenkinsagents:python'
            dockerHost 'unix:///var/run/docker.sock'
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

        booleanParam(name: 'skip_test', defaultValue: true, description: 'Set to true to skip the test stage')

    }
    triggers { pollSCM('H/2 * * * *') }
    stages {
        stage('Flow Control') {
            // when { expression { env.BRANCH_NAME != 'main' } }
            steps {
                echo 'I only execute on the ${env.BRANCH_NAME} branch'
            }
        }
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
                execute_stage('Deliver', params.skip_test)
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

def execute_stage(stage_name, skip) {
    stage(stage_name) {
        if(skip) {
            echo "Skipping ${stage_name} stage"
            return
        }
        // Add steps to test the application
    }
}