pipeline{
    agent any
    stages{
        stage('clone repo'){
            step{
                git url:"https://github.com/ancysnovee/data-structre.git",branch:"main"
            }
            
        }
        stage('Dependency'){
            step{
                echo 'installing dependencies'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                    '''

            }
        }
        stage ('test'){
            steps{
                echo 'running tests'
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                    '''
                    
            }
        }
        stage ('deploy'){
            steps{
                echo 'deploying application'
                bat '''
                    call venv\\Scripts\\activate
                    python createstack.py
                    '''
            }
        }
    }
}