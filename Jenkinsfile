pipeline {
    agent any

    environment {
        VENV = "venv"
        MY_VERSION = "1.0.0"
    }

    //adding parameters
    parameters {
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run tests?')
    }

    
    stages {
        
        // Custom Environment Variable
        stage('Build'){
            steps{
                 echo "Using version: ${MY_VERSION}"
                 bat "mvn -version"
            }
        }

        
        //conditional
        stage('Test') {
            when {
                expression { true }   // run only if condition is true
            }
            steps {
                echo 'Conditional Test Stage Running'
            }
            when {
                expression { params.executeTests == true }
            }
            steps {
                echo 'Running tests...'}
        }       
        
        stage('Checkout') {
            steps {
                echo "Pulling from GitHub..."
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment..."
                bat """
                    python -m venv %VENV%
                    call %VENV%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Test Application') {
            steps {
                echo "Testing Flask import..."
                bat """
                    call %VENV%\\Scripts\\activate
                    python -c "import app; print('Flask app imported successfully!')"
                """
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**', fingerprint: true
            }
        }

        stage('Deploy (Placeholder)') {
            steps {
                echo "Ready for deployment steps (Docker, SSH, etc.)"
            }
        }
    }

    post {
        always {
        echo 'This runs after every build'
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed."
        }
    }
}
