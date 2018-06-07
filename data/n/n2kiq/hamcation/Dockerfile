#FROM python:3.6  
FROM python:3-slim  
#FROM phusion/baseimage:latest  
# Use baseimage-docker's init system.  
#CMD ["/sbin/my_init"]  
LABEL maintainer="n2kiq0@gmail.com"  
  
EXPOSE 8888  
# Set the local timezone to US/Eastern or America/New_York  
ENV TZ=America/New_York  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Set the home directory to our app user's home.  
ENV HOME=/home/app  
ENV DATA=/home/app/data  
ENV APP_HOME=/home/app/hamcation  
  
# Create the home directory for the new app user.  
RUN mkdir -p $HOME $DATA  
  
# Create an app user so our program doesn't run as root.  
RUN groupadd -r app && useradd -r -g app -d $HOME -s /sbin/nologin -c "Docker
image user" app  
  
#RUN apt-get update && apt-get install -y mysql-client  
#RUN apt-get update && apt-get install -y python3-pip && apt-get clean && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# based on python:2.7-onbuild, but if we use that image directly  
# the above apt-get line runs too late.  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
COPY . $APP_HOME  
RUN pip install -r $APP_HOME/requirements.txt  
  
#RUN chown -R app:app $HOME $DATA  
RUN chown -R app:app $HOME  
  
USER app  
  
CMD ["python3", "/home/app/hamcation/server.py"]  

