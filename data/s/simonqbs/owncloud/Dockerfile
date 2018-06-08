FROM owncloud:8.2-fpm  
  
RUN \  
apt-get update && apt-get install --no-install-recommends -y cron smbclient \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl https://raw.githubusercontent.com/chrismytton/shoreman/master/shoreman.sh
-o /shoreman.sh \  
&& chmod +x /shoreman.sh  
  
RUN \  
rm -rf /etc/cron.*/* && sed -i '/m h/,$d' /etc/crontab \  
&& echo "*/15 * * * * www-data php -f /var/www/html/cron.php" >> /etc/crontab  
  
COPY entrypoint.sh /  
COPY Procfile /  
  
VOLUME ["/data"]  
  
CMD ["/shoreman.sh", "/Procfile"]  

