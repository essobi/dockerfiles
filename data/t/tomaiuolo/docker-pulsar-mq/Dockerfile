# Pulsar Message Queue  
# Download base image ubuntu 16.04  
FROM ubuntu:16.04  
MAINTAINER mariangela.tomaiuolo@ba.infn.it  
  
# Define the ENV variable  
ENV container docker  
  
#ARG DEBIAN_FRONTEND=noninteractive  
# Install pulsar, kombu, rabbitMQ  
RUN apt-get update && \  
apt-get install -y apt-utils \  
vim \  
python-dev \  
python-pip  
  
RUN pip install --upgrade pip  
  
RUN pip install virtualenv  
  
RUN mkdir -p /pulsar && \  
virtualenv /pulsar/venv && \  
. /pulsar/venv/bin/activate && \  
pip install pulsar-app \  
kombu  
RUN . /pulsar/venv/bin/activate && cd /pulsar && pulsar-config --mq  
  
# Avoid message: invoke-rc.d: policy-rc.d denied execution of start.  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
RUN apt-get install -y rabbitmq-server  
  
# Configure Port  
EXPOSE 8913 5672  
CMD . /pulsar/venv/bin/activate && cd /pulsar && pulsar  
  

