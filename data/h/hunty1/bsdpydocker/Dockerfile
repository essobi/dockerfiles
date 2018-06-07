# Dockerfile for BSDPy  
# All in one container, tftp, nginx and bsdpy  
# Graciously taken from Pepijn Bruienne's work  
# Version : Dev  
# Date : 04-05-15  
# BSDPy Commit : 8a011fc  
# Start from Debian to save space - about 100mb smaller than Ubuntu  
FROM debian:wheezy  
  
MAINTAINER Calum Hunter (calum.h@gmail.com)  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV BSDPY_IFACE eth0  
ENV BSDPY_IP 127.0.0.1  
ENV BSDPY_PROTO http  
  
# Add the packages we need from apt then remove the cached list saving some
disk space  
RUN apt-get -y update && \  
apt-get install -y curl \  
libxml2-dev \  
python \  
python-dev \  
python-pip \  
nginx \  
tftpd-hpa && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set up the directories and log files  
RUN mkdir /nbi && \  
mkdir /bsdpy && \  
touch /var/log/bsdpserver.log  
  
# Add all our files and scripts  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD start.sh /start.sh  
ADD bsdpserver.py /bsdpy/  
ADD __init__.py /bsdpy/  
ADD pydhcplib /bsdpy/pydhcplib  
ADD requirements.txt /  
  
# setup python  
RUN pip install -r requirements.txt  
  
# Ensure permissions are setup correctly  
RUN chown -R root:root /etc/nginx/nginx.conf && \  
chown -R root:root /start.sh && \  
chmod +x /start.sh /bsdpy/bsdpserver.py  
  
# Expose our ports to the world  
EXPOSE 67/udp  
EXPOSE 69/udp  
EXPOSE 80  
CMD /start.sh  
  

