FROM ubuntu:16.04  
MAINTAINER Kirill Sevryugin <kirill@sevryugin.ru>  
  
RUN \  
apt-get update \  
&& apt-get -y install \  
ruby-dev \  
build-essential \  
curl \  
wget \  
rpm \  
&& gem install fpm  
  
ENTRYPOINT ["fpm"]  
CMD ["--help"]  
  

