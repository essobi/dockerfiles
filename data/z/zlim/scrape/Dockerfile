FROM ubuntu  
MAINTAINER Zi Shen Lim <zlim.lnx@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
python \  
python-dev \  
python-pip \  
lib32z1-dev \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev  
  
RUN pip install scrapy  
RUN pip install service_identity  
  

