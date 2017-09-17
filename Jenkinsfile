pipeline {
  agent any
  stages {
    stage('SCM') {
      steps {
        git(url: 'git@github.com:lordoftheflies/django-jupyter-integration.git', branch: 'master', changelog: true, credentialsId: 'credentials-github-lordoftheflies-ssh', poll: true)
      }
    }
    stage('Install virtual environment') {
      steps {
        sh '''if [ ! -d "venv" ]; then
    virtualenv --no-site-packages -p /usr/bin/python3.4 venv
fi
'''
      }
    }
    stage('Setup') {
      steps {
        sh '''. ./venv/bin/activate
pip install -r kryten-notebook/requirements.txt
deactivate
'''
          }
      }
    stage('Build') {
      steps {
        sh '''. ./venv/bin/activate
cd kryten-notebook
python setup.py sdist develop
deactivate
'''
        }
    }
    stage('Test') {
      steps {
        sh '''. ./venv/bin/activate
cd kryten-notebook
# python -m unittest discover tests -p '*_test.py'
deactivate
'''
        sh '''. ./venv/bin/activate
cd pocsite
python manage.py test --no-input
deactivate
'''
      }
    }
    stage('Deploy staging') {
      steps {
        sh '''. ./venv/bin/activate
cd kryten-notebook
python setup.py sdist install
deactivate
'''
      }
    }
    stage('Update version') {
      steps {
        sh '''. ./venv/bin/activate
VERSION=$(cat kryten-notebook/notebook/version.py | grep "__version__ = " | sed 's/__version__ =//' | tr -d "'")
echo "$VERSION"
bumpversion --allow-dirty --message 'Jenkins Build {$BUILD_NUMBER} bump version of module: {current_version} -> {new_version}' --commit --current-version $VERSION patch kryten-notebook/notebook/version.py
deactivate
'''
        sh '''git push origin master
'''
      }
    }
    stage('Distribute') {
      steps {
        sh '''. ./venv/bin/activate
cd kryten-notebook
python setup.py sdist upload -r local
deactivate
'''

      }
    }
  }
}