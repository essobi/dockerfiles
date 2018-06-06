FROM phusion/baseimage:0.9.22  
LABEL maintainer=chouandy  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV DOCKER_VERSION=17.12.1~ce-0~ubuntu  
  
# Upgrade Packages  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Install Packages  
RUN apt-get update && apt-get install -y \  
git \  
tzdata  
  
# Install AWS Cli  
RUN apt-get install -y python-dev  
RUN curl 'https://bootstrap.pypa.io/get-pip.py' -o 'get-pip.py'  
RUN python get-pip.py  
RUN pip install awscli  
RUN rm -f get-pip.py  
  
# Install Docker  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y docker-ce=$DOCKER_VERSION  
  
# Install docker-compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
# Finalize  
RUN apt-get remove -y autoconf automake \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

