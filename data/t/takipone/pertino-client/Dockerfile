FROM ubuntu:14.04  
MAINTAINER Pertino Inc. "developer@pertino.com"  
MAINTAINER takipone "takipone@gmail.com"  
# Install Pertino Dependencies ------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
isc-dhcp-client \  
net-tools \  
libpcap0.8-dev \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Pertino -----  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
F7E3CA0F7A008E65A1C5C0A7DD2CF55E326BD77B  
RUN echo 'deb http://reposerver.pertino.com/debs precise multiverse' >
/etc/apt/sources.list.d/pertino.list  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -y -q pertino-client || true  
  
# Move dhclient to avoid issue with AppArmor  
# See https://github.com/docker/docker/issues/5490  
RUN mv /sbin/dhclient /usr/sbin/dhclient  
  
RUN mkdir -p /etc/resolvconf  
  
# Set runtime commands  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

