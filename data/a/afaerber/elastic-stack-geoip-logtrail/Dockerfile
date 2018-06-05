FROM blacktop/elastic-stack:geoip  
  
RUN kibana-plugin install
https://github.com/sivasamyk/logtrail/releases/download/0.1.8/logtrail-5.2.0-0.1.8.zip  
CMD ["/sbin/tini","--","/usr/bin/supervisord","-c",
"/etc/supervisor/supervisord.conf"]  

