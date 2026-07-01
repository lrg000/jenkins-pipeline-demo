pipeline {
    agent any

    stages {

        stage('拉取代码') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/lrg000/jenkins-pipeline-demo.git'
            }
        }

        stage('检查环境') {
            steps {
                bat 'python --version'
            }
        }

        stage('运行 Python') {
            steps {
                bat 'python main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline 执行成功'
        }
        failure {
            echo '❌ Pipeline 执行失败'
        }
    }
}