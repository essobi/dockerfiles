FROM ubuntu:latest  
  
MAINTAINER louis <louis@systemli.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y make ruby1.9.3 curl nmap dnsutils  
RUN \  
apt-get install -y wget unzip && \  
cd /tmp && \  
wget
https://github.com/nabla-c0d3/sslyze/releases/download/release-0.11/sslyze-0_11-linux64.zip
&& \  
unzip sslyze-0_11-linux64.zip && rm sslyze-0_11-linux64.zip && \  
cd /tmp/sslyze-0_11-linux64 && mv sslyze /opt && \  
ln -s /opt/sslyze/sslyze.py /usr/local/bin/sslyze && \  
wget https://github.com/sqlmapproject/sqlmap/archive/0.6.2.tar.gz && \  
tar xf 0.6.2.tar.gz && \  
mv sqlmap-0.6.2 /opt/sqlmap && \  
ln -s /opt/sqlmap/sqlmap.py /usr/local/bin/sqlmap && \  
apt-get purge -y unzip wget && apt-get autoremove -y && apt-get autoclean &&
rm -rf /tmp/*  
RUN gem install gauntlt  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
CMD gauntlt  

