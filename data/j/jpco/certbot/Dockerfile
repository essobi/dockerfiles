FROM codingwell/rpi-raspbian-qemu  
  
MAINTAINER J.P.C. Oudeman  
  
#  
# Mounts: - /etc/letsencrypt  
# - /var/www  
#  
# Set noninteractive mode for apt-get  
ENV DEBIAN_FRONTEND=noninteractive \  
EMAIL=webmaster@example.loc \  
DOMAINS="www.example.loc"  
RUN [ "cross-build-start" ]  
# Install packages  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-key adv --recv-key --keyserver keyserver.ubuntu.com 8B48AD6246925553 && \  
apt-key adv --recv-key --keyserver keyserver.ubuntu.com 7638D0442B90D010 && \  
apt-get update && \  
apt-get install -y certbot -t jessie-backports && \  
# Cleanup  
apt-get clean && \  
find /var/lib/apt/lists /tmp /var/tmp /var/log -type f -delete  
RUN [ "cross-build-end" ]  
  
WORKDIR /root  
ADD assets/cli.ini /root  
  
ENTRYPOINT ["/usr/bin/certbot"]  
CMD ["renew"]  

