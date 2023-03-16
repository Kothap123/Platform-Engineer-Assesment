pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'GIT_URL'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install requests'
                sh 'pip install beautifulsoup4'
            }
        }
        
        stage('Test') {
            steps {
                sh 'source venv/bin/activate'
                sh 'python -m unittest discover -s tests -p "*sample.py"'
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "Building command-line tool..."'
                sh 'pyinstaller dictionary.py --onefile'
            }
        }
        
        stage('Package') {
            steps {
                sh 'echo "Creating artifact..."'
                sh 'mkdir -p artifacts'
                sh 'cp dist/dictionary artifacts'
            }
        }
        
        stage('Define Word') {
            steps {
                sh 'source venv/bin/activate'
                sh 'artifacts/dictionary exercise'
            }
        }
        
        stage('Display Definition') {
            steps {
                sh 'echo "Definition: ${def}"'
            }
        }
    }
}
