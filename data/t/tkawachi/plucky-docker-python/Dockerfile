FROM ubuntu:14.04  
MAINTAINER Takashi Kawachi <kawachi@p-lucky.net>  
  
RUN apt-get update  
RUN apt-get install -y python-dev libmysqlclient-dev python-scipy gfortran \  
python-pip  
RUN apt-get install -y git  
RUN pip install git+https://github.com/pLucky-
Inc/pyloess.git@befcee14784e0ca3f00f5c64ccfa449ee28ddbca  
RUN pip install pandas flask-sqlalchemy mysql-python uwsgi  

