FROM debian:wheezy  
  
MAINTAINER Frank Wilson <frank@zenlambda.com>  
  
RUN apt-get update -y && \  
apt-get install -y curl \  
net-tools \  
procps \  
python \  
python-numpy && \  
curl -sSL https://github.com/kanaka/noVNC/archive/v0.5.tar.gz \  
| tar zxf -  
  
CMD ["/noVNC-0.5/utils/launch.sh"]  
  
EXPOSE 6080  

