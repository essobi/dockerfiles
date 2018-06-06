FROM ubuntu:15.10  
MAINTAINER Jamgo Coop <info@jamgo.coop>  
  
# Install required packages  
RUN set -x; \  
apt-get update && \  
apt-get install -y --no-install-recommends git openconnect python-mechanize
iptables supervisor && \  
cd /root && \  
git clone -c http.sslVerify=false https://github.com/jamgocoop/juniper-vpn-
py.git && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get purge --auto-remove -y git  
  
COPY startup.sh /root/startup.sh  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN echo "[supervisord]" > /etc/supervisord.conf && \  
echo "nodaemon=true" >> /etc/supervisord.conf && \  
echo "" >> /etc/supervisord.conf && \  
echo "[program:startup]" >> /etc/supervisord.conf && \  
echo "command=/root/startup.sh" >> /etc/supervisord.conf && \  
echo "stdout_logfile=/dev/fd/1" >> /etc/supervisord.conf && \  
echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf && \  
echo "autorestart=false" >> /etc/supervisord.conf && \  
echo "startretries=0" >> /etc/supervisord.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

