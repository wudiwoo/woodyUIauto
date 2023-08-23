pipeline {
    agent {
        docker {
            // 指定要使用的本地 Docker 镜像
            image 'python:3.8'
            args '--privileged' // 如果需要特权访问
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // 从 GitHub 检出代码，credentialsId 是您的 GitHub 凭据的 ID。
                git credentialsId: 'tester', url: 'https://github.com/wudiwoo/woodyUIauto.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                // 安装应用程序依赖
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // 在容器内运行测试脚本
                sh 'python test_runner.py'
            }
        }

        stage('Publish Test Report') {
            steps {
                script {
                    // 发布 HTML 测试报告
                    def reportDir = pwd() + '/reports'
                    def reports = findFiles(glob: "$reportDir/*.html")
                    def latestReport = reports[reports.size() - 1]
                    publishHTML(target: [allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'htmlreports', reportFiles: latestReport, reportName: 'HTML Report', reportTitles: ''])
                }
            }
        }
    }
}
