FROM debian:8.6  
LABEL version="0.1.0" description="Debian with pandas for base images"  
MAINTAINER Victor Clark <victor@victorclark.org>  
  
#Install some useful tools:  
RUN \  
apt-get update && \  
apt-get install -y \  
ipython \  
python \  
python-dev \  
python-pip  
  
RUN pip install pandas  
#Need to replace sh with bash for compiling source  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
#Put out the welcome mat  
WORKDIR /  
ENTRYPOINT /bin/bash  

