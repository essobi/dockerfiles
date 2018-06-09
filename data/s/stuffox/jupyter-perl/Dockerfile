FROM ubuntu:14.04  
MAINTAINER Tudor Marghidanu  
  
ENV JUPYTER_PORT 8080  
ENV JUPYTER_IP 0.0.0.0  
ENV JUPYTER_NOTEBOOK_DIR /opt/jupyter  
  
# Installing dependencies  
RUN apt-get update && apt-get install -y build-essential curl \  
python-dev \  
python-pip \  
pkg-config \  
libcairo2-dev \  
libzmq3-dev  
  
RUN pip install jupyter  
  
# Installing IPerl without tests ...  
RUN curl -sL http://cpanmin.us | perl - App::cpanminus \  
&& /usr/local/bin/cpanm --notest Devel::IPerl \  
PDL \  
Moose \  
MooseX::AbstractFactory \  
MooseX::AbstractMethod \  
MooseX::Storage \  
Test::More  
  
EXPOSE $JUPYTER_PORT  
  
VOLUME $JUPYTER_NOTEBOOK_DIR  
  
RUN mkdir -p $JUPYTER_NOTEBOOK_DIR  
WORKDIR $JUPYTER_NOTEBOOK_DIR  
  
ENTRYPOINT iperl notebook --port $JUPYTER_PORT \--ip $JUPYTER_IP \--notebook-
dir $JUPYTER_NOTEBOOK_DIR  

