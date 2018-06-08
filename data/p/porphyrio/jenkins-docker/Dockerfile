# VERSION 1.0  
# AUTHOR: Porphyrio  
# DESCRIPTION: jenkins container  
# BUILD: docker build --rm -t porphyrio/jenkins-docker:v0.9 .  
FROM jenkins  
MAINTAINER porhyrio  
  
# if we want to install via apt  
USER root  
  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
netcat \  
curl \  
python-pip \  
python-dev \  
libmysqlclient-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
&& pip install ansible==1.9.4 \  
&& pip install https://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm
\  
&& pip install boto \  
&& pip install awscli  
  
COPY configuration /usr/share/jenkins/ref/  
COPY plugins/plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
VOLUME /root/.ssh

