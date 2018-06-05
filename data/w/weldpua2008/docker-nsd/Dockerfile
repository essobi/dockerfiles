# Dockerfile for building Ansible image for Ubuntu 12.04 (Precise LTS), with
as few additional software as possible.  
FROM ubuntu:12.04  
  
MAINTAINER Valeriy Solovyov <weldpua2008@gmail.com>  
RUN echo "===> Updating cache..." && \  
apt-get update && \  
\  
\  
echo "===> Installing nsd3..." && \  
apt-get install -y -o Dpkg::Options::="--force-confold" \--force-yes nsd3
openssl && \  
\  
\  
apt-get clean && \  
\  
\  
rm -f /etc/nsd3/nsd.conf && \  
touch /etc/nsd3/nsd.conf && \  
mkdir -p /var/run/nsd3  
#&& \  
#zonec -c /etc/nsd3/nsd.conf  
  
  
# Volumes  
# /etc/nsd3 : configuration and zone files  
# /var/log/nsd : log files  
VOLUME ["/etc/nsd3", "/var/log/nsd"]  
  
EXPOSE 53/udp 53/tcp  
  
#CMD ["nsd", "-d"]  
  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

