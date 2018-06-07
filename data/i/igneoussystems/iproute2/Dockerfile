FROM debian:wheezy  
  
RUN echo deb http://http.debian.net/debian wheezy-backports main > \  
/etc/apt/sources.list.d/wheezy-backports.list  
  
RUN apt-get update && apt-get -t wheezy-backports install -y iproute2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y bridge-utils \  
&& rm -rf /var/lib/apt/lists/*  

