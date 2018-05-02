## run markdown as robot file



## test register

    python3 setup.py register -r pypitest
    or
    twine register --repository-url https://test.pypi.org/legacy/ -r pypitest robot-md-launcher

## test upload

    python3 setup.py sdist upload -r pypitest
    or
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    
## dist register

    python3 setup.py register -r pypi
    or
    twine register -r pypi robot-md-launcher
    
## dist upload
    python3 setup.py sdist upload -r pypi
    or
    twine upload dist/*


## notice 
    .pypirc:
    [pypitest]
    repository=https://test.pypi.org/legacy
    
    [pypi]
    repository=https://pypi.org/legacy