# https://docs.docker.com/engine/articles/dockerfile_best-practices/  
FROM ubuntu:16.04  
MAINTAINER JP <jportela@abyssal.eu>  
  
# Install locales so we can use locale-gen command.  
RUN apt-get update && apt-get install -y locales  
  
# LOCALE/LANG settings. Having this properly setup, avoids multiple
installation issues.  
RUN locale-gen en_US.UTF-8  
ENV LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"
PYTHONIOENCODING="utf-8"  
RUN apt-get update && apt-get install --no-install-recommends -yq \  
python3-all \  
python3-setuptools \  
python3-pip \  
# using pip, psycopg2 has a lot of dependencies and too long to install,
prefer apt.  
python3-psycopg2 \  
# so that we can call nosetests command.  
python3-nose \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip && pip3 install teamcity-messages  
  
WORKDIR /code  

