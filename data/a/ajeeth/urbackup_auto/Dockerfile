FROM phusion/baseimage:0.9.19  
MAINTAINER ajeeth.samuel@gmail.com  
  
# Initialize Ubuntu  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
  
# add repo, update apt and install build dependencies  
add-apt-repository ppa:uroni/urbackup && \  
apt-get update -q && \  
apt-get upgrade -y openssl && \  
apt-get install -y nginx ca-certificates socat wget unzip nfs-common
libcurl4-openssl-dev iputils-ping net-tools inotify-tools && \  
apt-get download -y urbackup-server  
  
# Nginx configurations  
RUN mkdir /etc/service/nginx  
ADD scripts/service-nginx.sh /etc/service/nginx/run  
RUN chmod 775 /etc/service/nginx/run && \  
chown -R www-data:www-data /var/lib/nginx && \  
rm /etc/nginx/sites-enabled/default && \  
rm /etc/nginx/sites-available/default  
  
# Add Urbackup nginx conf  
ADD scripts/urbackup-nginx.conf /etc/nginx/sites-available/urbackup  
RUN ln -s /etc/nginx/sites-available/urbackup /etc/nginx/sites-enabled/default  
  
# Interface the environment  
RUN mkdir /opt/urbackup  
VOLUME /opt/urbackup/certs  
VOLUME /opt/urbackup/log  
#VOLUME /media/BACKUP  
VOLUME /var/urbackup  
EXPOSE 443 55415  
EXPOSE 35623/udp  
  
RUN apt-get autoremove -y  
  
ENV USEEXTVOL false  
ENV NFSSHARE /opt/fusecompress:/media/BACKUP  
  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  
  
# Add urbackup start script  
ADD scripts /root/scripts  
RUN chmod +x /root/scripts/*.sh && touch /first_run  
  
# clean up  
RUN apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
CMD ["/root/scripts/start.sh"]  

