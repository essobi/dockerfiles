FROM jarischaefer/docker-librenms  
  
RUN echo '*/5 * * * * librenms . /etc/librenms_environment;
/opt/librenms/html/plugins/Weathermap/map-poller.php >> /dev/null 2>&1' >>
/etc/cron.d/librenms  

