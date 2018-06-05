# DOCKER-VERSION 1.1.2  
# VERSION 0.1  
FROM debian:wheezy  
MAINTAINER Justin Plock <justin@plock.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -q wget debhelper automake \  
libapr1-dev libpcre3-dev libssl-dev libdbi-dev libcap-dev \  
libexpat1-dev libtool libperl-dev autotools-dev xmlto dblatex  
  
RUN wget -q -O - http://softlayer-dal.dl.sourceforge.net/project/nxlog-
ce/nxlog-ce-2.8.1248.tar.gz | tar -xzf - -C /opt  
WORKDIR /opt/nxlog-ce-2.8.1248/packaging/debian  
RUN sh make_debs.sh  
RUN dpkg -i /opt/nxlog-ce_2.8.1248_amd64.deb  
RUN apt-get purge -y -q xmlto dblatex  
RUN apt-get autoremove -y -q  
  
EXPOSE 514/tcp 514/udp  
  
ENTRYPOINT ["/usr/bin/nxlog"]  
CMD ["-f"]  

