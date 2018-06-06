# VERSION 0.5  
# DOCKER-VERSION 1.2.0  
# AUTHOR: Milo de Vries <milo@xdh.nl  
# DESCRIPTION: Ruby+Packer+AWS tools to macke some clouds  
  
# this is 2.2, alternatively downgrade with :2.1-slim  
FROM ruby:slim  
  
run apt-get update && apt-get -y install --no-install-recommends \  
curl \  
unzip \  
jq \  
colordiff \  
git \  
awscli \  
ssh-client \  
build-essential \  
pkg-config \  
cmake \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean all  
  
# Since ruby:slim is really slim, we could consider fat  
# FROM ruby  
  
# Get AWS cli (requirement python-pip)  
# RUN pip install awscli  
  
# Run Packer script  
COPY ./packer.sh /  
RUN /packer.sh  
  
# Install sloww gems  
RUN gem install nokogiri rugged  
  
# env var example:  
# ENV RVM_DIR /usr/local/rvm/  
# ENV PATH $PATH:$RVM_DIR/bin  

