# jmvrbanc/cafe-runner  
#  
# Docker image for running CloudCAFE jobs  
# Ubuntu 14.04 (Trusty)  
#  
# How to Run:  
# sudo docker run -v {HOST_DIR}:/cafe/volume -t jmvrbanac/cafe-runner {ARGS}  
#  
FROM ubuntu:latest  
MAINTAINER John Vrbanac <john.vrbanac@linux.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev git  
  
# Initial Clone  
RUN mkdir -p /cafe/  
RUN git clone https://github.com/CafeHub/opencafe.git /cafe/opencafe  
RUN git clone https://github.com/stackforge/cloudcafe.git /cafe/cloudcafe  
RUN git clone https://github.com/stackforge/cloudroast.git /cafe/cloudroast  
  
# Hack to make pip work LP Bug #1306991  
RUN easy_install requests  
  
# Install now to avoid pulling all dependencies at runtime  
RUN pip install /cafe/opencafe/; pip install /cafe/cloudcafe/; pip install
/cafe/cloudroast/  
  
# Add execution scripts  
COPY run.sh /cafe/run.sh  
COPY update.sh /cafe/update.sh  
  
VOLUME ["/cafe/volume"]  
ENTRYPOINT ["/bin/sh", "/cafe/run.sh"]  

