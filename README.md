## run markdown as robot file

## build
    python3 setup.py sdist
 
## test upload

    python3 setup.py sdist upload -r pypitest
    # or upload only 
    twine upload  -r pypitest dist/*
  
## dist upload
    python3 setup.py sdist upload
    # or upload only
    twine upload dist/*


## notice 
    .pypirc:
    [pypitest]
    repository=https://test.pypi.org/legacy/
    
     