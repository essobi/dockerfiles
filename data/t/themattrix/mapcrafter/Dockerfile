FROM ubuntu:14.04  
# proper init  
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini /tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /  
  
RUN apt-get update && \  
apt-get -y install python curl wget apt-transport-https && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "deb https://packages.mapcrafter.org/ubuntu $(lsb_release -sc) main"
| tee "/etc/apt/sources.list.d/mapcrafter.list" && \  
wget -O "/etc/apt/trusted.gpg.d/mapcrafter.gpg"
"http://packages.mapcrafter.org/ubuntu/keyring.gpg"  
  
RUN apt-get update && \  
apt-get -y install mapcrafter && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD render.conf ./  
  
CMD ["mapcrafter", "-c", "./render.conf", "-j", "2"]  

