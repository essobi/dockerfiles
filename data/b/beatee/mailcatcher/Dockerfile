#  
# High five for https://github.com/zolweb/docker-
mailcatcher/blob/master/Dockerfile - Thanks!  
#  
# This image exists just to utilise the latest Ubuntu LTS  
#  
FROM ubuntu:16.04  
  
MAINTAINER Jan Klan <jan@beatee.org>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -q -y \  
libsqlite3-dev \  
ruby \  
ruby-dev \  
build-essential \  
&& gem install --no-ri --no-rdoc mailcatcher \  
&& apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
EXPOSE 1080 1025  
  
ENTRYPOINT ["mailcatcher", "--smtp-ip=0.0.0.0", "--http-ip=0.0.0.0", "--
foreground"]  

