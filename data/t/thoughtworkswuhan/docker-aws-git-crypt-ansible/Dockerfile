FROM newbieguide/docker_ansible  
MAINTAINER Baiyuan Wang<bywang.thoughtworks.com>  
  
ENV VERSION 0.5.0-2  
USER root  
RUN apk --update add \  
bash \  
curl \  
git \  
g++ \  
make \  
openssh \  
openssl \  
openssl-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -L https://github.com/AGWA/git-crypt/archive/debian/$VERSION.tar.gz |
tar zxv -C /var/tmp  
RUN cd /var/tmp/git-crypt-debian-$VERSION && make && make install
PREFIX=/usr/local && rm -rf /var/tmp/*  
RUN apk del make openssl-dev  

