## run markdown as robot file



## test

    python3 setup.py register -r pypitest

## test upload

    python setup.py sdist upload -r pypitest
    
## dist

    python setup.py register -r pypi
    
## dist upload
    python setup.py sdist upload -r pypi


## notice 
    .pypirc:
    [pypitest]
    repository=https://test.python.org/pypi