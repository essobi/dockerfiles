FROM buildpack-deps:jessie  
  
RUN apt-get update && apt-get install -y \  
build-essential autoconf libtool \  
&& apt-get clean  
  
COPY install.sh /tmp/install.sh  
RUN bash /tmp/install.sh  

