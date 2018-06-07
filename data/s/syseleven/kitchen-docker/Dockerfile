# docker build -f Dockerfile-kitchen-docker -t syseleven/kitchen-docker .  
FROM ubuntu:16.04  
MAINTAINER Stefan Andres <s.andres@syseleven.de>  
ENV container docker  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install system  
RUN apt-get update && apt-get install --no-install-recommends -y curl ruby2.3
ruby2.3-dev \  
apt-transport-https ca-certificates curl software-properties-common libffi-dev
\  
build-essential rsync ssh-client git jq locales  
  
# Generate locales  
RUN locale-gen en_US.UTF-8 && update-locale  
  
# Install Docker  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - &&
\  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
apt update && apt-get install --no-install-recommends -y docker-ce  
  
# Add GNU parallel recent version  
ADD http://ftp.gnu.org/gnu/parallel/parallel-20160522.tar.bz2
/tmp/parallel.tar.bz2  
RUN cd /tmp && tar xvjpf parallel.tar.bz2 && \  
cd parallel-20160522 && \  
./configure && \  
make && \  
make install && rm -rf /tmp/parallel*  
  
# Install kitchen deps  
ADD Gemfile /root/  
RUN cd /root && gem install --no-ri --no-rdoc bundler && \  
bundler install  

