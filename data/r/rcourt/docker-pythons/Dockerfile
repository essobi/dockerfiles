FROM debian:stretch  
LABEL maintainer "Louis Paternault <spalax+docker@gresille.org>"  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN echo 'APT::Default-Release "stretch";' > /etc/apt/apt.conf.d/99default-
release  
RUN echo 'deb http://httpredir.debian.org/debian buster main' >
/etc/apt/sources.list.d/buster.list  
RUN \  
apt-get --yes update && \  
apt-get install --yes \  
python \  
python-pip \  
python-dev \  
&& \  
apt-get install --yes \  
python3 \  
python3-dev \  
python3-pip \  
&& \  
apt-get install --yes \  
pypy \  
pypy-dev \  
&& \  
apt-get install --yes \  
jython \  
&& \  
apt-get install --yes \--target-release stretch \  
python3.5 \  
python3.5-dev \  
&& \  
apt-get install --yes \--target-release buster \  
python3.6 \  
python3.6-dev \  
&& \  
apt-get clean  
RUN pip install tox  
  
# Print versions  
RUN for bin in python python2.7 python3 python3.5 python3.6 pypy jython tox; \  
do \  
echo "$bin $($bin --version 2>&1)"; \  
done  

