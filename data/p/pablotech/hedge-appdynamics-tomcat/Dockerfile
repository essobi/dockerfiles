FROM pablotech/hedge-tomcat:latest  
  
#APPDYNAMICS FOR WEB APPS: TOMCAT  
RUN wget http://hedge-it.s3.amazonaws.com/AppServerAgent-4.2.12.0.zip  
RUN unzip AppServerAgent-4.2.12.0.zip -d /opt/; mkdir -p
/opt/ver4.2.12.0/logs/Tomcat/; chmod 777 -R /opt/ver4.2.12.0  
RUN echo "export CATALINA_OPTS=\"$CATALINA_OPTS
-javaagent:/opt/ver4.2.12.0/javaagent.jar\"" >>
/usr/share/tomcat7/bin/setenv.sh  
RUN chmod 777 /usr/share/tomcat7/bin/setenv.sh  
RUN rm -rf /usr/share/tomcat7/webapps  
RUN ln -s /var/lib/tomcat7/webapps/ /usr/share/tomcat7/webapps  
RUN sed -i '/exit 0/c\\\n' /etc/rc.local  
  
#PORTS  
# 22 ssh, 80 http, 443 https, 1194 vpn, 5900 tightVNC  
EXPOSE 22/tcp 80/tcp 443/tcp 1194/udp 5900/tcp 8080/tcp 8090/tcp  
  
  

