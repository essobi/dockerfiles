FROM ubuntu:12.04  
LABEL maintainer "Matthew Schwartz @schwartz1375"  
  
WORKDIR /root  
USER root  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && apt-get -y \  
dist-upgrade && apt-get clean && apt-get install -y \  
ca-certificates nmap vim wget ssh \  
perl libnet-socks-perl libnet-cidr-perl  
  
WORKDIR /opt  
RUN wget https://www.snort.org/downloads/community/community-rules.tar.gz &&
tar xf community-rules.tar.gz  
  
WORKDIR /tmp  
RUN wget -O inundator https://bitbucket.org/schwartz1375/docker-
inundator/raw/23707d4b8885623b91daa07fd1dd1fbb22fd9d89/inundator.pl  
RUN mv inundator /usr/bin/inundator && chmod +x /usr/bin/inundator  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  

