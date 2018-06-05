FROM mdrolc/node:latest  
  
COPY . /var/www/  
VOLUME /var/www/data  
  
RUN cd /var/www/ && \  
yarn install && \  
mkdir -p ./data/screenshots && \  
chown -R www-data . && \  
chsh -s /bin/bash www-data && \  
{ crontab -l -u www-data; echo '@hourly /usr/bin/node $HOME/scrape.js'; } |
crontab -u www-data -  
  
CMD ["/var/www/start.sh"]  

