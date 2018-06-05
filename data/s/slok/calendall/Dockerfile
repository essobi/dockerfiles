FROM python:3.4.2  
MAINTAINER Xabier Larrakoetxea <slok69@gmail.com>  
  
ENV PYTHONUNBUFFERED 1  
# System dependencies  
RUN apt-get update && \  
apt-get -y -q install git\  
libpq5\  
libpq-dev\  
nodejs\  
npm  
  
# Hack for node binary  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install psql on steroids  
RUN pip install pgcli  
  
# Project Python dependecies  
RUN git clone https://github.com/calendall/calendall.git /tmp/calendall  
RUN pip install -r /tmp/calendall/requirements/dev.txt  
RUN rm -rf /tmp/calendall  
  
# Project Extra dependencies  
RUN npm install -g bower yuglify  
  
# Create the user/group for the running stuff  
RUN groupadd -g 1000 calendall  
RUN useradd -m -u 1000 -g 1000 calendall  
  
RUN mkdir /code  
RUN chown calendall:calendall /code  
WORKDIR /code  
  
USER calendall  
  
EXPOSE 8000  
VOLUME /data  

