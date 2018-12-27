pipeline {
    agent any

    environment {
        VIRTUAL_ENV_PATH = "${env.WORKSPACE}/venv"
        VIRTUAL_ENV_ACTIVATOR = "${VIRTUAL_ENV_PATH}/bin/activate"
        REPORTS_PATH = "${env.WORKSPACE}/reports"
        PYTHON_BASE_INTERPRETER_PATH = "/usr/bin/python3m"
    }

    stages {
        stage('Prepare environment') {
            steps {
                echo "Preparing clean build environment"
                sh """
                rm -Rf ${REPORTS_PATH} && mkdir ${REPORTS_PATH}
                rm -Rf ${VIRTUAL_ENV_PATH} && mkdir ${VIRTUAL_ENV_PATH}
                """
            }
        }

        stage('Create virtualEnv') {
            steps {
                sh '${PYTHON_BASE_INTERPRETER_PATH} -m venv ${VIRTUAL_ENV_PATH}'
            }
        }

        stage('Install requirements') {
            steps {
                sh """
                . ${VIRTUAL_ENV_ACTIVATOR}
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('PyLint') {
            steps {
                sh """
                . ${VIRTUAL_ENV_ACTIVATOR}
                pip install pylint
                pylint pdm | tee ${REPORTS_PATH}/pylint.log
                """
            }
        }

        stage('UT') {
            steps {
                sh """
                . ${VIRTUAL_ENV_ACTIVATOR}
                python -m unittest pdm.tests | tee ${REPORTS_PATH}/ut.log
                """
            }
        }
    }

    post {
        always {
            dir ("${REPORTS_PATH}"){
                archiveArtifacts artifacts: "*.log", onlyIfSuccessful: true
            }
        }
    }
}
