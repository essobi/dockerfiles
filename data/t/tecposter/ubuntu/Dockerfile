FROM ubuntu:16.04  
MAINTAINER "zhanjh@126.com"  
COPY sources.list /etc/apt/sources.list  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
&& rm -rf /var/lib/apt/lists/*  
#&& apt-get install --no-install-recommends --no-install-suggests -y \  
#gcc \  
#build-essential \  
#make \  
#libpcre3 libpcre3-dev \  
#openssl libssl-dev \  
#curl  
CMD ["/bin/bash"]  

