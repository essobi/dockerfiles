FROM phusion/baseimage  
  
MAINTAINER MartyTremblay  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \--no-install-recommends \  
wget \  
python \  
python-dev \  
python-pip \  
python-virtualenv  
  
RUN wget -q -O - http://archive.getdeb.net/getdeb-archive.key | apt-key add \-
&& \  
sh -c 'echo "deb http://archive.getdeb.net/ubuntu yakkety-getdeb apps" >>
/etc/apt/sources.list.d/getdeb.list'  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \--no-install-recommends \  
ncid \  
&& \  
apt-get purge -y \--auto-remove && rm -rf /var/lib/apt/lists/*  

