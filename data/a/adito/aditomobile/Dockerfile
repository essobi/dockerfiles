FROM tomcat:9.0-jre8-alpine  
  
ADD start.sh /start.sh  
  
RUN chmod +x /start.sh \  
&& apk add --no-cache wget \  
&& rm -rf /usr/local/tomcat/webapps/* \  
&& mkdir -p /usr/local/tomcat/webapps/aditomobile \  
&& wget -q
"https://files.weptun.de/index.php?action=show&what=file&hash=a55a04f0cf.war"
-O /tmp/aditomobile.war \  
&& unzip -q /tmp/aditomobile.war -d /usr/local/tomcat/webapps/aditomobile \  
&& rm -rf /tmp/*  
  
CMD ["/start.sh"]

