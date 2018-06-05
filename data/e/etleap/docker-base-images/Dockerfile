# Follow https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/ when possible :)  
  
FROM ubuntu:xenial  
  
RUN apt-get -q update && apt-get -q -y upgrade && apt-get install --no-
install-recommends -y \  
awscli \  
git \  
golang-go\  
python3-pip \  
python3-setuptools \  
ssh \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip shyaml docker-compose==1.16.1  
  
RUN wget -qO-
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz |
tar xz --strip-components 1 -C /usr/bin  

