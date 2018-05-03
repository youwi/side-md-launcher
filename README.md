## run markdown as side file
now only support selenium keywords.
- for SeleniumIDE.
- only support sidexx keywords.

## usage
    python -m side_md_launcher *.side
    
## syntax

- support markdown syntax(heading table): (sidexx keywords):

 
    |         |                                        |              |
    |---------|----------------------------------------|--------------|
    | open    | /wiki/Main_Page                        |              |
    | clickAt | id=searchInput                         |              |
    | type    | id=searchInput                         | Selenium IDE |
    | clickAt | css=.mw-searchSuggest-link:first-child |              |

- support vertical line sep file (sidexx keywords)


    | open    | /wiki/Main_Page                        |              |
    | clickAt | id=searchInput                         |              |
    | type    | id=searchInput                         | Selenium IDE |
    | clickAt | css=.mw-searchSuggest-link:first-child |              |

- support html file(TODO)

```
    < table >< tr >< td >.....< /table >
```

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
    
     