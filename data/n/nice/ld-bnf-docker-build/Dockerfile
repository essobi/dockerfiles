# TODO bump to latest or 4.2.2.30 ?  
FROM mono:4.2.1.102  
MAINTAINER Patrick McEvoy <patrick@qmtech.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get install -y libxml2-utils git mercurial  
  
RUN apt-get install curl && \  
curl --silent --location https://deb.nodesource.com/setup_4.x | bash - &&\  
apt-get install --yes nodejs  
  
RUN mkdir /code  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

