# shiv_package_tutorial

Show how to shiv your product into one-file for distribution with shiv. 

> same as https://shiv.readthedocs.io/en/latest/django.html

- requirements.txt
  - pip install -r requirements.txt

- runtime.txt
  - python shebang like: /usr/bin/env python or python3
- dist folder
  - product main packages, entry_point should be main function of app  module by default.
- shiv_me.py
  - run that : python3 shiv_me.py, will generate a zip file named app.pyz , which can be used as python3 app.pyz or double click on windows.
