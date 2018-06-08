FROM opsbears/supervisord:stable  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nullmailer && mkfifo
/var/spool/nullmailer/trigger && chown mail:root /var/spool/nullmailer/trigger
&& chmod 0622 /var/spool/nullmailer/trigger  
COPY usr/ /usr  
COPY etc/ /etc

