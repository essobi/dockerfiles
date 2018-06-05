FROM ubuntu:16.04  
MAINTAINER Abdul Somat Budiaji "abdulbudiaji@gmail.com"  
RUN apt-get update && apt-get install -y \  
wget \  
ca-certificates \  
\--no-install-recommends  
  
# install salt with master  
RUN wget -O -
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| apt-key add -  
RUN echo deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial
main | tee /etc/apt/sources.list.d/saltstack.list  
RUN apt-get update && apt-get install -y \  
salt-minion \  
\--no-install-recommends  
  
# clean up  
RUN rm -rf /var/lib/apt/lists/*  

