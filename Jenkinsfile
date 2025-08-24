@Library('my-shared-lib') _

node('master') {   // هنا نضمن التشغيل على Jenkins master
    // Parameters
    properties([
        parameters([
            choice(name: 'LANG', choices: ['python'], description: 'Choose language'),
            string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build'),
            string(name: 'PARALLEL_WORKERS', defaultValue: '2', description: 'Number of parallel workers')
        ])
    ])

    def lang = params.LANG
    def branch = params.BRANCH
    def workers = bounds.toInt(params.PARALLEL_WORKERS, 1, 5)

    stage('Checkout') {
        checkout([$class: 'GitSCM',
                  branches: [[name: "*/${branch}"]],
                  userRemoteConfigs: [[url: 'https://github.com/USERNAME/python-ci-simple.git']]])
    }

    // Parallel jobs
    def jobs = [:]
    for (int i = 1; i <= workers; i++) {
        def idx = i
        jobs["worker-${idx}"] = {
            stage("Build-${idx}") {
                sh "echo '🔧 Running worker ${idx} on master'"
                sh "python3 main.py ${idx}"
            }
            stage("Test-${idx}") {
                sh """
                python3 -m venv .venv || true
                . .venv/bin/activate
                pip install -r requirements.txt
                pytest -q || true
                """
            }
        }
    }

    stage('Parallel Build') {
        parallel jobs
    }
}
