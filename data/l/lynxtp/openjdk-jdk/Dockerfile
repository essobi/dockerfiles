FROM lynxtp/openjdk-jre:8  
MAINTAINER "Tom Vaughan <tvaughan@lynxtp.com>"  
  
RUN apt-get -q update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -q -y install \  
openjdk-8-jdk=* \  
&& apt-get -q clean \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["javac"]  

