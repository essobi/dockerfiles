FROM debian:jessie  
  
MAINTAINER WHITEPLUS System "sysadmin@wh-plus.com"  
  
ENV BEANSTALKD_VERSION 1.10  
  
RUN apt-get update \  
&& apt-get install -y curl build-essential \  
# download  
&& curl -sL
https://github.com/kr/beanstalkd/archive/v${BEANSTALKD_VERSION}.tar.gz | tar
xvz -C /tmp \  
# build and install  
&& cd /tmp/beanstalkd-${BEANSTALKD_VERSION} \  
&& make \  
&& cp beanstalkd /usr/bin \  
# cleanup package manager  
&& apt-get remove --purge -y curl build-essential \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

