FROM ubuntu:16.04  
MAINTAINER Danny Arnold <despair.blue@gmail.com>  
  
RUN apt update  
  
# Yarn  
RUN apt install -y nodejs curl apt-transport-https ca-certificates curl gnupg2
software-properties-common  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
RUN apt update && apt install -y yarn  
  
# Node  
RUN yarn global add n  
RUN n 8  
  
RUN apt-get remove --purge -y $(apt-mark showauto) curl apt-transport-https
ca-certificates curl gnupg2 software-properties-common  
RUN rm -rf /var/lib/apt/lists/*  

