FROM debian:wheezy  
  
MAINTAINER Shawn Sit <xueqingxiao@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y python-pip  
RUN pip install shadowsocks==2.8.2 && \  
apt-get purge -y --auto-remove $buildDeps  
  
ENTRYPOINT ["/usr/local/bin/ssserver"]

