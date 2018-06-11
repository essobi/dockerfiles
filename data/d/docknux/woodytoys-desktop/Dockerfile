FROM ubuntu:latest  
MAINTAINER Denis Pettens <denis.pettens@gmail.com>  
  
# Isntall some useful programs  
RUN set -x \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server htop
iproute2 moreutils ssh nano vim net-tools dnsutils iputils-ping telnet alpine
\  
&& rm -rf /var/lib/apt/lists/*  
  
# Config sshd  
RUN set -x \  
&& mkdir /var/run/sshd  
  
# Set environment variables for squid proxy  
ENV http_proxy=http://squid.wt6.ephec-ti.be:3128/ \  
https_proxy=http://squid.wt6.ephec-ti.be:3128/ \  
ftp_proxy=http://squid.wt6.ephec-ti.be:3128/ \  
no_proxy=localhost,127.0.0.1  
# Some programs use uppercase variants  
ENV HTTP_PROXY=http://squid.wt6.ephec-ti.be:3128/ \  
HTTPS_PROXY=http://squid.wt6.ephec-ti.be:3128/ \  
FTP_PROXY=http://squid.wt6.ephec-ti.be:3128/ \  
NO_PROXY=localhost,127.0.0.1  
EXPOSE 4022  
CMD ["/usr/sbin/sshd", "-D", "-p", "4022"]  

