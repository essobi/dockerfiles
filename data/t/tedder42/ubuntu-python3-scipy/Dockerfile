FROM ubuntu:14.04  
# debian based; https://github.com/docker-
library/openjdk/blob/master/openjdk-8-jre/Dockerfile  
# pip can fail on localefoo with Ubuntu. It exhibits with a
UnicodeDecodeError.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
#ENV LANGUAGE en_US:en  
#ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -y python3 python3-scipy python3-pip
python3-dev libpq-dev python3-dev libffi-dev  
RUN pip3 install --upgrade pip==8.1.2  
RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN pip install awscli  
  
CMD mkdir -p /opt/app  
VOLUME /opt/  
VOLUME /usr/src/app/  
  
ADD requirements.txt /opt/app/requirements.txt  
RUN pip install -r /opt/app/requirements.txt  
# RUN  
# CMD  

