FROM buildpack-deps:jessie  
# Install System libraries  
RUN apt-get update && apt-get install -y \  
git \  
nginx \  
supervisor \  
awscli \  
&& rm -rf /var/lib/apt/lists/*  
  
# Expose 80  
EXPOSE 80  
# Setup  
RUN mkdir -p /app /var/log/app \  
&& rm -f /etc/nginx/sites-enabled/* \  
&& chown -R www-data:www-data /app /var/log/app  
  
# Configuration  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY app.conf /etc/nginx/sites-enabled/  
COPY supervisord.conf /etc/supervisor/  
  
# Entrypoint command  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf" ]  
  

