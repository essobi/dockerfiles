FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y curl cron && \  
curl -O https://dl.eff.org/certbot-auto && \  
mv certbot-auto /usr/local/bin/ && \  
chmod +x /usr/local/bin/certbot-auto && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "*/57 * * * * root certbot-auto -n renew" >> /etc/crontab && \  
chmod 600 /etc/crontab  
  
CMD /usr/sbin/cron -f  

