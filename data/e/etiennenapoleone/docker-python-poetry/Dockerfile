FROM python:3.7-rc  
  
MAINTAINER Etienne Napoleone <etienne_napo@hotmail.com>  
  
# install python and poetry  
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-
poetry.py | python  
  
# create application directory  
RUN mkdir /app  
WORKDIR /app  
  
# copy pyproject file  
ONBUILD COPY pyproject.* .  
  
# install dependencies:  
ONBUILD RUN poetry install -n  
  
# using this file  
# ~~~~~~~~~~~~~~~  
# FROM etiennenapoleone/docker-python-poetry  
# COPY . /app  
# CMD python3 main.py  

