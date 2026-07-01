pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('拉取代码') {
            steps {
                checkout scm
            }
        }

        stage('环境检查') {
            steps {
                bat 'python --version'
            }
        }

        stage('安装依赖') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('运行测试') {
            steps {
                bat 'pytest -v'
            }
        }

        stage('运行主程序') {
            steps {
                bat 'python main.py'
            }
        }
    }

    post {
        success {
            echo "✅ 测试通过 + 构建成功"
        }

        failure {
            echo "❌ 测试失败，Pipeline中断"
        }
    }
}