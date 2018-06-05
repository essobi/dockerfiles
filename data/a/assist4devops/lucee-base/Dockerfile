FROM tomcat:8.0.41-jre8  
  
MAINTAINER krushik <krushik@assist.ru>  
ENV LUCEE_VERSION 5.1.0.34  
ENV LUCEE_JARS_URL
http://release.lucee.org/rest/update/provider/loader/$LUCEE_VERSION  
ENV LUCEE_JAVA_OPTS "-Xms256m -Xmx512m"  
# Download core JAR, and delete it in one step to avoid committing the
installer in a FS layer  
RUN wget -nv $LUCEE_JARS_URL -O /root/lucee.jar && \  
mkdir -p /usr/local/tomcat/lucee && \  
cp /root/lucee.jar /usr/local/tomcat/lucee/lucee.jar && \  
rm -rf /root/lucee.jar  
  
# Delete the default Tomcat webapps so they aren't deployed at startup  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# Set Tomcat config to load Lucee  
COPY catalina.properties server.xml web.xml /usr/local/tomcat/conf/  
  
# Custom setenv.sh to load Lucee  
COPY setenv.sh /usr/local/tomcat/bin/  
RUN chmod a+x /usr/local/tomcat/bin/setenv.sh  
  
# Create Lucee configs  
COPY lucee-server.xml /opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
  
# Merge log dirs  
RUN ln -s /usr/local/tomcat/logs /opt/lucee/server/lucee-server/context/logs
&& \  
ln -s /usr/local/tomcat/logs /opt/lucee/web/logs  
  
# Provide test page  
RUN mkdir -p /var/www  
COPY index.cfm /var/www/  
ONBUILD RUN rm -rf /var/www/*  
  
# lucee first time startup; explodes lucee and installs bundles/extensions  
RUN /usr/local/tomcat/bin/catalina.sh start && \  
while [ ! -f "/opt/lucee/web/logs/application.log" ] ; do sleep 2; done && \  
echo -n "test app page: "; wget -q http://127.0.0.1:8888/ && echo OK && \  
echo -n "server admin page: "; wget -qO-
http://127.0.0.1:8888/lucee/admin/server.cfm | grep -q "button submit" && echo
OK && \  
/usr/local/tomcat/bin/catalina.sh stop 2>/dev/null && rm -f --
/usr/local/tomcat/logs/*  
  
# Replace the Trusted SSL Certificates packaged with Lucee with those from
Debian  
# ca-certificates package from the OS is the most recent authority  
RUN cp -f /etc/ssl/certs/java/cacerts /opt/lucee/server/lucee-
server/context/security/cacerts  

