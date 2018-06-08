FROM lynxtp/ubuntu:15.10  
MAINTAINER "Tom Vaughan <tvaughan@lynxtp.com>"  
  
RUN apt-get -q update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -q -y install \  
openjdk-8-jre-headless=* \  
&& apt-get -q clean \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["java"]  

