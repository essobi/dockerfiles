FROM docker.io/debian:latest  
MAINTAINER Edgard Castro <castro@edgard.org>  
  
# Keep image updated  
ENV VERSION 3.0.13.3  
# Configure dpkg  
RUN echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/docker-no-
recommends && \  
echo 'APT::Install-Suggests "false";' > /etc/apt/apt.conf.d/docker-no-suggests
&& \  
echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/docker-assume-yes &&
\  
echo 'APT::Get::Show-Upgraded "true";' > /etc/apt/apt.conf.d/docker-show-
upgraded && \  
echo 'APT::Quiet "true";' > /etc/apt/apt.conf.d/docker-quiet && \  
echo 'DPkg::Options { "--force-confmiss"; "--force-confnew" };' >
/etc/apt/apt.conf.d/docker-force-config  
  
# Update base system and install software  
RUN apt-get update && \  
apt-get dist-upgrade && \  
apt-get install curl bzip2 && \  
curl -LS
http://dl.4players.de/ts/releases/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2
| tar jxC /tmp && \  
mv /tmp/teamspeak3-server_linux_amd64 /opt/teamspeak && \  
apt-get purge curl bzip2 && \  
apt-get autoremove --purge && \  
apt-get clean && \  
rm -rf /var/lib/apt /tmp/* /var/tmp/*  
  
# Add custom files  
COPY files/root /  
  
# Exposed ports and volumes  
VOLUME ["/data"]  
EXPOSE 9987/udp 10011 30033  
# Start command  
CMD ["/start.sh"]  

