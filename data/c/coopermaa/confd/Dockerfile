FROM debian:wheezy  
MAINTAINER MAINTAINER coopermaa77@gmail.com  
  
# (1) Install confd  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install curl && \  
cd /usr/local/bin && \  
curl -fsSL
https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-
amd64 -o confd && \  
chmod a+x confd  
  
# (2) Add confd and haproxy templates  
ADD etc/confd/ /etc/confd  
  
CMD /usr/local/bin/confd -debug -verbose -interval 20 -node $ETCD  

