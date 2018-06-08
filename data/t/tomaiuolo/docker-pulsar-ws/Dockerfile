# Pulsar Web Server  
# Download base image ubuntu 16.04  
FROM ubuntu:16.04  
MAINTAINER mariangela.tomaiuolo@ba.infn.it  
  
# Define the ENV variable  
ENV container docker  
  
#ARG DEBIAN_FRONTEND=noninteractive  
# Install pulsar  
RUN apt-get update && \  
apt-get install -y apt-utils \  
git \  
vim \  
python-dev \  
python-pip \  
libffi-dev \  
libssl-dev  
  
RUN pip install --upgrade pip  
  
RUN git clone https://github.com/galaxyproject/pulsar.git /pulsar  
  
RUN pip install virtualenv  
  
RUN virtualenv /pulsar/.venv && \  
. /pulsar/.venv/bin/activate &&\  
pip install -r /pulsar/requirements.txt &&\  
pip install pyOpenSSL  
  
RUN cp /pulsar/server.ini.sample /pulsar/server.ini &&\  
cp /pulsar/app.yml.sample /pulsar/app.yml  
  
# Avoid message: invoke-rc.d: policy-rc.d denied execution of start.  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
# Configure Port  
EXPOSE 8913  
CMD . /pulsar/.venv/bin/activate && cd /pulsar && ./run.sh  

