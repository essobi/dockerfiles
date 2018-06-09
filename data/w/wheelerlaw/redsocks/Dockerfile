FROM ubuntu:16.04  
MAINTAINER Wheeler Law <whelderwheels613@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential curl iptables-dev
libevent-dev \  
&& curl -fsSL https://github.com/darkk/redsocks/archive/release-0.5.tar.gz |
tar xz \  
&& make -C redsocks-release-0.5/  
  
# Use a multi-stage build to cut down on image size  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y iptables net-tools libevent-2.0-5
libevent-core-2.0-5  
COPY \--from=0 redsocks-release-0.5/redsocks /usr/local/bin  
  
COPY redsocks.tmpl /etc/redsocks.tmpl  
COPY entrypoint.sh /entrypoint.sh  
COPY fw.sh /fw.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

