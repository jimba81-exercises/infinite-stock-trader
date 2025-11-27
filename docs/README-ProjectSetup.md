# Infinite Stock Trader - Project Setup

## Table of Contents
1. [Project Info](#1-project-info)
2. [Docker Environment](#2-docker-environment)
3. [Python Project Setup](#3-python-project-setup)

<br>

# 1. Project Info
- Type: Python

<br>

# 2. Docker Environment

## 2.1. Create Dev Docker Image
```console
$ cd ${PROJECT_PATH}

$ # Build dev docker image
$ docker compose build dev
```

## 2.2. Setup Environment
> Use `DEV Docker Image` to setup the project
```console
$ cd ${PROJECT_PATH}
$ mkdir -p workspace

$ # Ensure permission access is resolved between host and docker environment
$ sudo chmod -R o+w . 

$ # Run dev docker container
$ docker compose run --rm dev bash

dev-docker$ ## Develop within docker container..
```

<br>

# 3. Python Project Setup

## 3.1. Init Poetry Project
>Reference: https://python-poetry.org/docs/cli/
```sh
$ poetry --version ## Ensure poetry works and version is returned
$ cd ${WORKSPACE}
$ rm -rf ./venv # Ensure exsitng ./venv is clear
$ poetry init # Init Poetry project, set params (e.g. package name)

$ poetry run python main.py # Run app

$ poetry add <some dependency>
```



<br>