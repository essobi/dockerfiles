FROM nextcode/baseimg-java:oracle-jdk10  
  
MAINTAINER WuXi NextCODE DevOps <devops@wuxinextcode.com>  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends git python python-pip curl lsof
unzip && \  
pip install virtualenv && \  
curl -fsSL https://apt.dockerproject.org/gpg | apt-key add \- && \  
add-apt-repository "deb https://apt.dockerproject.org/repo/
ubuntu-$(lsb_release -cs) main" && \  
apt-get update && \  
apt-get -y install docker-engine && \  
rm -rf /var/lib/apt/lists/* && \  
locale-gen en_US.UTF-8 && \  
groupadd builder && \  
adduser --disabled-password --gecos "" \--ingroup builder builder  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

