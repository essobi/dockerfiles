FROM python:3  
ENV PYTHONUNBUFFERED 1  
# Passed in from docker-compose file  
ARG mode  
  
USER root  
  
WORKDIR /code  
RUN apt-get update && apt-get install -y ruby ruby-dev && rm -rf
/var/lib/apt/lists/*  
RUN gem install sass --version 3.5.6  
ADD requirements/*.txt /code/requirements/  
RUN pip install --upgrade pip  
RUN pip install -r requirements/$mode.txt  
RUN pip install git+https://github.com/kevindice/django-allauth@0500a25e37  
  
RUN groupadd -r appuser -g 1000 \  
&& useradd -u 1000 -r -g appuser -s /bin/false -c "App User" appuser \  
&& chmod -R 755 /code  
  
USER appuser  

