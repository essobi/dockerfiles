FROM debian:wheezy  
MAINTAINER Kalamangga.Net R&D  
COPY sources.list /etc/apt/  
RUN apt-get update && \  
apt-get upgrade -y --force-yes && \  
apt-get clean -y --force-yes  
RUN apt-get install -y --force-yes nano && \  
apt-get clean -y --force-yes  
CMD ["/bin/bash"]  

