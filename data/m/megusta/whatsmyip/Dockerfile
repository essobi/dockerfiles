FROM ubuntu:14.04  
MAINTAINER christoph@megusta.ag  
ENV CREATED_AT 2014-12-20  
RUN apt-get update -qq && \  
apt-get upgrade -qqy && \  
apt-get install nano wget curl software-properties-common -qqy && \  
apt-get clean -qqy && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD lookup.sh /lookup.sh  
  
ENTRYPOINT ["/lookup.sh"]  

