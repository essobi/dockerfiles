FROM ubuntu:14.04  
MAINTAINER Iain Mckay <me@iainmckay.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV ETCD_IP 172.17.42.1  
ENV ETCD_PORT 4001  
ENV S3_OBJECT etcd.json  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get upgrade -yq \  
&& apt-get install -yq --no-install-recommends git jq/trusty-backports nodejs
npm python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& pip install awscli  
  
RUN npm install -g git+https://github.com/sekka1/etcd-dump.git  
#ADD ./ /opt/app  
#WORKDIR /opt/app  
#RUN npm install  
ADD start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  

