pipeline {
    agent any

    environment {
        VIRTUAL_ENV_PATH = "${env.WORKSPACE}/venv"
        VIRTUAL_ENV_ACTIVATOR = ". ${VIRTUAL_ENV_PATH}/bin/activate &> /dev/null"
        REPORTS_PATH = "${env.WORKSPACE}/reports"
        PYTHON_BASE_INTERPRETER_PATH = "/opt/rh/rh-python36/root/usr/bin/python"
    }

    stages {
        stage('Prepare environment') {
            steps {
               script {
                    currentBuild.description = "<b>HASH:</b> ${GIT_COMMIT}"
                }
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
                ${VIRTUAL_ENV_ACTIVATOR}
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('PyLint') {
            steps {
                sh """
                ${VIRTUAL_ENV_ACTIVATOR}
                pip install pylint==2.1.1
                pylint pdm --ignore=tests --rcfile=config.rcfile | tee ${REPORTS_PATH}/pylint.log
                """
            }
        }

        stage('UT') {
            steps {
                sh """
                ${VIRTUAL_ENV_ACTIVATOR}
                python -m unittest  discover pdm.tests
                """
            }
        }
    }

    post {
        always {
            dir ("${REPORTS_PATH}"){
                archiveArtifacts artifacts: "pylint.log"
            }
        }
    }
}
