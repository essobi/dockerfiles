FROM larsks/carbon-base  
  
EXPOSE 2003  
EXPOSE 2004  
EXPOSE 7002  
COPY init-carbon-cache-config.sh /entrypoint.d/init-carbon-cache-config.sh  
CMD ["/usr/bin/carbon-cache", "--nodaemon", \  
"--config=/etc/carbon/carbon.conf", \  
"--logdir=/var/log/carbon/", \  
"start"]  
  

