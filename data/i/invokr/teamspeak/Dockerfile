# Based on overshard/docker-teamspeak  
FROM centos:7  
MAINTAINER Robin Dietrich <me@invokr.org>  
  
# Teamspeak version to download  
ENV tsv=3.0.13.4  
# Upgrade base system  
RUN yum update -y && yum upgrade -y && yum install bzip2 wget -y && yum clean
all  
  
# Install teamspeak  
ADD
http://dl.4players.de/ts/releases/${tsv}/teamspeak3-server_linux_amd64-${tsv}.tar.bz2
./  
RUN tar xf teamspeak3-server_linux_amd64-${tsv}.tar.bz2 \  
&& mv teamspeak3-server_linux_amd64 /opt/teamspeak \  
&& rm teamspeak3-server_linux_amd64-${tsv}.tar.bz2 \  
&& useradd -s /sbin/nologin teamspeak \  
&& mkdir -p /ts/log \  
&& chown -R teamspeak:teamspeak /opt/teamspeak /ts  
  
# Install init  
ADD scripts/init /init  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
# Teamspeak ports  
EXPOSE 9987/udp  
EXPOSE 30033  
EXPOSE 10011  
# Run  
WORKDIR /ts  
USER teamspeak  
CMD ["/usr/local/bin/dumb-init", "/init"]  

