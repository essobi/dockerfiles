FROM drupaldocker/drush  
MAINTAINER drupal-docker <info@drupaldocker.org>  
  
VOLUME /var/backups  
  
COPY run.sh /root/  
  
RUN chmod +x /root/run.sh \  
&& echo "\$options[\"structure-tables\"][\"common\"] = array(\"cache\",
\"cache_*\", \"history\", \"search_*\", \"sessions\", \"watchdog\");" >>
/root/.drush/drushrc.php  
  
ENV DRUPAL_ROOT=/var/www/html \  
SITE_FOLDER=default  
  
CMD ["/root/run.sh"]  

