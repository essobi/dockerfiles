FROM ubuntu:16.04  
  
ARG PDNS_VERSION=3.4.9-1  
ARG PDNS_PUBKEY=0x7EED19F3  
ARG PDNS_KEYSERVER=pool.sks-keyservers.net  
  
MAINTAINER Wido den Hollander <wido@widodh.nl>  
  
RUN apt-get -y update && apt-get install -y curl  
  
RUN cd /tmp \  
&& curl -L -o pdns.asc https://downloads.powerdns.com/releases/deb/pdns-
static_${PDNS_VERSION}_amd64.deb.asc \  
&& curl -L -o pdns.deb https://downloads.powerdns.com/releases/deb/pdns-
static_${PDNS_VERSION}_amd64.deb \  
&& gpg --keyserver ${PDNS_KEYSERVER} --recv-keys ${PDNS_PUBKEY} \  
&& gpg --verify pdns.asc pdns.deb \  
&& dpkg -i pdns.deb \  
&& rm pdns.deb pdns.asc  
  
COPY pdns.conf /etc/powerdns/pdns.conf  
  
EXPOSE 53  
  
CMD ["pdns_server", "--daemon=no"]  

