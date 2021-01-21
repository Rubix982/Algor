# CS302 - Algorithms Project

<p align="left">
 <a href="#">
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Django" src="https://img.shields.io/badge/Django-Django?style=for-the-badge&logo=django&color=092E20"/>
<img alt='Heroku' src="https://img.shields.io/badge/Heroku-Heroku?style=for-the-badge&logo=heroku&color=430098"/>
<img alt="LaTeX" src="https://img.shields.io/badge/latex%20-%23008080.svg?&style=for-the-badge&logo=latex&logoColor=white"/>
<img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>
<img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
<img alt="HTML" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>
<img alt="CSS" src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>
 </a>
</p>

## Table Of Contents

- [Description](#description)
- [Intent And Idea](#intent-and-idea)
- [File Structure](#file-structure)
    - [apps](#apps)
    - [config](#config)
    - [cs302AlgorithmsProject](#cs302algorithmsproject)
    - [Root Files](#root-files)
- [Datasets Generation](#datasets-generation)
- [Collectstatic And Migrations](#collectstatic-and-migrations)
- [OS Details Which Was Used](#os-details-which-was-used)

## Description

This is a semester project - The perfect Dynamic Programming Algorithms Project. This is a submission for the CS 302 course offered @ FAST NUCES, under Sir Zeeshan Khan and Sir Waqas Sheikh. It's meant to serve as a very simply Django application that helps you select an algorithm from a list of Dynamic Algorithms, and a datasets for viable for at least of the algorithms given.

The application then takes the two components, uses the dataset in the algorithm, and displayts the output on a new page. The report for the project has been attached as well.

## Intent And Idea

As required for the project requirements, a GUI application with a 'very nice UI' was needed, which meant to help or serve as a way to ease and see the results obtained from the GUI application.

## File Structure

### apps

Django splits the responsibility from the main MVC view into smaller 'components' and applications that each handle their responsibilities quite easily. 

Inside of `apps` is `base`, where the source code for the,

- Algorithms
- Templates
- Urls
- Views
- Static files

exist.

You can find all the algorithms within `apps/base/src/`, except in `apps/base/src/aux.py`, which helps to mitigate what algorithm and dataset is to be used by removing the abstraction level from the view logic and shifting it over to the business logic.

`apps/base/src/aux.py` has the datasets embedded within its source code, which it takes, and then sends it over to the respective targeted algorithms to be rendered for the results.

The `apps/base/static/base` contains the `css/` and `js/` folders, which have the source files for manipulating the CSS and Javascript for the components that exist within `apps/base/templates`. 

The responsibility to take care of the views has been shifted from the main source repository in `cs302AlgorithmsProject` to `apps/base/templates` to facilitate with ease what HTML files to render.

The main home page is in `home.html`, the final result page uses `result`, the about page uses `about`, the contact page uses `contact`, the report page uses the `report` option.

### config

Hopefully no changes will be needed here for the average user, but to describe, this folder contains the `NGINX` and `WSGI` settings to enable the routing and the HTTP protocols. It specifies from `WSGI` parameters that are helpful to have, as well as some loggin related.

The `NGINX` configurations specify the headers, the default ports, the pages to render when an internal or external error arises, does redirection, deals with caching, specifies the location for the MIME types, and sets the default character format to `chartset-utf-8`.

### cs302AlgorithmsProject

This contains the,

- Settings
- Static files
- Templates

The `Settings` directory contains the files that tell Django what the variables or configurations are used for the `development` and `production` environment. In practice, use the `development` ( default ) settings when you want to test out changes locally as a developer in real time, as hot-reloading is supported here. Use `production` when you want to see what the final result will look when you push this to deploy somewhere, for example, on `AWS`, `Azure`, `GCP`, `CloudFlare`, `CloudFront`, `Redhat`, or like the default option used here, `Heroku`.

The `Static Files` most notably uses `base.html` that is extended to the `templates` within `apps/base/templates/home.html` that control the extension of the format and details the footer, the header, the imports for the CS, JS, and `CDN` files. The other `*.html` files here.

The `urls.py` and `wsgi.py` are self-explanatory. 

### Root Files

- .editorconfig: Specifies the styling, to be left upto Django and editorconfigs, if needed
- .gitignore: Specifies what files should be ignored by Git
- makefile: Shortcut for commands, `make dev` for dev server, `make prod` for production server, `make static` for collectstatic command, `make noinput`, to specify the `--noinput` flag as well
- manage.py: Main file to used wth Django to start and close the project
- Pipfile: Used by `pipenv` to keep a local store of the files used
- Pipfile.lock: Again, used by `pipenv` for locking versions of pacakges
- Procfile: For deploying to heroku
- Project_Desc.pdf: The original requirement specification for the project in this semester
- readme.md: Contains the instructions for the developer, running, building, debugging, pulled off as a template for a repository
- README.md: This file!
- requirements.txt: Specifies the dependencies that live in the `virtualenv` or `pipenv` whichever is used
- runtime.txt: Specifies the `Python` version used for the development
- tox.ini: Some basic packages needed to initialize the component

## Building The Application

To deal with,

- Using `pipenv`
- Using `collecstatic`
- Using `development` environment
- Using `production` environment

Please take a look at `readme.me`.

## Datasets Generation

The code that was used to generate the dataset is uploaded here, https://gist.github.com/Rubix982/c95be3be0a5de615e37fdcd7c474be44

This was a quick .py file for generating the data for us.
Works for `(d)`, `(e)`, `(f)`, `(g)`, `(h)`, `(i)`, `(j)`.

We used this https://www.careerbless.com/calculators/word/list.php to generate the string permutations for the datasets needed in `(a)`, `(b)`, `(c)`.

## OS Details Which Was Used

- Operating System: Kubuntu 20.04
- KDE Plasma Version: 5.18.5
- KDE Frameworks Version: 5.68.0
- Qt Version: 5.12.8
- Kernel Version: 5.4.0-62-generic
- OS Type: 64-bit
- Processors: 8 × Intel® Core™ i7-8665U CPU @ 1.90GHz
- Memory: 15.5 GiB of RAM