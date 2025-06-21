pipeline {
    agent any
//   triggers {
//         // Uncomment if you want scheduled runs (e.g., every day at 7 AM)
//         // cron('H 7 * * *')
//
//         // Uncomment if you want auto-trigger on Git changes
//         pollSCM('* * * * *')
//     }
    parameters {
        choice(name: 'BROWSER', choices: ['edge', 'chrome', 'firefox'], description: 'Browser name')
        choice(name: 'MARKER', choices: ['smoke', 'all', 'sanity'], description: 'Test group')
        choice(name: 'PARALLEL', choices: ['1','2','3'], description: 'Threads')
    }

    environment {
        REPORT_DIR = "reports"
        ALLURE_RESULTS = "${REPORT_DIR}\\allure-results"
        ALLURE_HTML = "${REPORT_DIR}\\allure-html"
    }

    stages {

        stage('Initialize') {
            steps {
                echo 'Initializing pipeline...'
            }
        }

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Madhan-091296/TutorialNinja'
            }
        }

        stage('Clean Reports') {
            steps {
                echo "Cleaning previous reports..."
                bat "rmdir /s /q %ALLURE_RESULTS% || exit 0"
                bat "rmdir /s /q %ALLURE_HTML% || exit 0"
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def marker = params.MARKER
                    def markerOption = marker == 'all' ? '' : "-m ${marker}"
                    def testCommand = "call venv\\Scripts\\activate.bat && pytest -s -v ${markerOption} --alluredir=%ALLURE_RESULTS% -n ${params.PARALLEL} testCases\\ --browser ${params.BROWSER}"
                    echo "Running tests with command: ${testCommand}"
                    bat "${testCommand}"
                }
            }
        }

        stage('Generate Allure HTML Report') {
            steps {
                echo "Generating Allure HTML report..."
                bat "allure generate %ALLURE_RESULTS% -o %ALLURE_HTML% --clean"
            }
        }

        stage('Publish Allure Report in Jenkins') {
            steps {
                echo "Publishing Allure report in Jenkins UI..."
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: "${ALLURE_HTML}/**", fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Always publishing Allure results..."
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: "${env.ALLURE_RESULTS}"]]
        }

        success {
//             mail to: 'mmr091296@gmail.com, kmr91296@gmail.com',
//                  subject: "✅ Jenkins Job: ${env.JOB_NAME} #${env.BUILD_NUMBER} - SUCCESS",
//                  body: """Build completed successfully!,
//                  from: 'Madhan <mmr091296@gmail.com>'
//
// Job: ${env.JOB_NAME}
// Build: #${env.BUILD_NUMBER}
// Report: ${env.BUILD_URL}allure
// Logs: ${env.BUILD_URL}console
// """
emailext(
            to: 'mmr091296@gmail.com, kmr91296@gmail.com',
            subject: "✅ Jenkins Job: ${env.JOB_NAME} #${env.BUILD_NUMBER} - SUCCESS",
            body: """
                <p>Hello Team,</p>

                <p>The Jenkins job has completed successfully.</p>

                <ul>
                    <li><strong>Job:</strong> ${env.JOB_NAME}</li>
                    <li><strong>Build:</strong> #${env.BUILD_NUMBER}</li>
                    <li><strong>Report:</strong> <a href="${env.BUILD_URL}allure">${env.BUILD_URL}allure</a></li>
                    <li><strong>Logs:</strong> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></li>
                </ul>

                <p>Regards,<br>Madhan's Jenkins</p>
            """,
            mimeType: 'text/html'
        )
        }

        failure {
            mail to: 'mmr091296@gmail.com',
                 subject: "❌ Jenkins Job: ${env.JOB_NAME} #${env.BUILD_NUMBER} - FAILURE",
                 body: """Build failed.

Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}
Report: ${env.BUILD_URL}allure
Logs: ${env.BUILD_URL}console
"""
        }
    }
}
