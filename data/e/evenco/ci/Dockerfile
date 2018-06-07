# NOTE: keep up to date with what we use in `evenco/even-server`  
FROM circleci/golang:1.10.1  
  
# Base image includes, among other things:  
# go  
# docker  
# docker-compose  
# Install Python + AWS CLI  
ADD requirements.txt /tmp/requirements.txt  
  
RUN mkdir -p /tmp/build \  
&& cd /tmp/build \  
&& sudo apt-get update \  
&& sudo apt-get install python python3 \  
&& wget \--quiet https://bootstrap.pypa.io/get-pip.py \  
&& sudo python3 get-pip.py \  
&& sudo pip install -r /tmp/requirements.txt \  
&& wget \--quiet https://s3.amazonaws.com/aws-cli/awscli-bundle.zip \  
&& unzip awscli-bundle.zip \  
&& sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& sudo apt-get clean \  
&& sudo rm -rf /var/lib/apt/lists/* \  
&& sudo rm -rf /tmp/build /tmp/requirements.txt  
  
# Go tools  
RUN go get -u gopkg.in/alecthomas/gometalinter.v2 \  
&& gometalinter.v2 \--install  

