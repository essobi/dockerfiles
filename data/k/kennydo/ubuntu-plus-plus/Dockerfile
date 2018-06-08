FROM ubuntu:14.04.4  
  
MAINTAINER chinesedewey@gmail.com  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-get install -y \  
python3 \  
python3-pip \  
git-all \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
libjpeg-dev \  
libpng-dev \  
libpq-dev \  
ntp \  
mysql-client  
  
RUN add-apt-repository ppa:maxmind/ppa -y \  
&& apt-get update \  
&& apt-get install -y \  
libmaxminddb0 \  
libmaxminddb-dev \  
mmdb-bin  

