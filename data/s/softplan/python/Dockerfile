FROM python:3.6-alpine  
  
RUN apk update --no-cache && \  
apk upgrade \--no-cache && \  
apk add \--no-cache build-base  
  
RUN pip install --upgrade pip  
RUN pip install coverage flake8 pytest tox pytest-cov mock  

