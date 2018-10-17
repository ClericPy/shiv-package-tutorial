# shiv package tutorial

Show how to shiv your product into one-file for distribution with shiv. 

> same as https://shiv.readthedocs.io/en/latest/django.html

## Usage

```python3 shiv_me.py```


## Details

- requirements.txt
  - `pip install -r requirements.txt`

- runtime.txt
  - python shebang like: `/usr/bin/env python3`(Linux) or `python3`(Win32)
- dist folder
  - product main packages, entry_point should be main function of app  module by default.
- shiv_me.py
  - run like this: `python3 shiv_me.py`, then will generate a zip file named `app.pyz`, which can be used as `python3 app.pyz` or `./app.pyz` or even double click on windows.
