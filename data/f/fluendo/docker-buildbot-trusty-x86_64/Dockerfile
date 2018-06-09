FROM ubuntu:14.04  
MAINTAINER fluendo  
  
# Install required packages  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
python2.7 \  
python2.7-dev \  
python-setuptools \  
python-pip \  
git && \  
pip install -U pip setuptools  
  
# Install buildbot requirements  
RUN pip install buildbot-worker  
RUN mkdir /worker  
  
# Environment variables required by buildbot  
ENV BUILDMASTER example-master  
ENV BUILDMASTER_PORT 9076  
ENV WORKERNAME example-worker  
ENV WORKERPASS example-pass  
  
WORKDIR /worker  
COPY run.sh .  
CMD ["./run.sh"]  

