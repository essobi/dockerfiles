FROM bitnami/nginx  
  
RUN apt-get update && apt-get install -y curl cron && \  
curl -O https://dl.eff.org/certbot-auto && \  
mv certbot-auto /usr/local/bin/ && \  
chmod +x /usr/local/bin/certbot-auto && \  
certbot-auto --os-packages-only --noninteractive  
  
RUN echo "*/57 * * * * root certbot-auto renew" >> /etc/crontab  
  
RUN sed -i '/check_for_updates &/a cron &' /app-entrypoint.sh  

