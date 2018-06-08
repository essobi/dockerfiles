FROM nginx:1.13.8  
RUN apt-get update \  
&& apt-get install -y letsencrypt \  
supervisor \  
&& apt-get install -y --no-install-recommends cron \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /etc/letsencrypt \  
&& mkdir -p /var/www/letsencrypt \  
&& mkdir -p /var/log/letsencrypt  
  
COPY supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/etc/cron.d", "/var/www/letsencrypt", "/etc/letsencrypt",
"/var/log/letsencrypt"]  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

