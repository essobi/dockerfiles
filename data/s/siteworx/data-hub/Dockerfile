FROM siteworx/hybris-beta  
  
###############################################################################  
# Tomcat  
###############################################################################  
  
RUN wget http://ftp.wayne.edu/apache/tomcat/tomcat-7/v7.0.67/bin/apache-
tomcat-7.0.67.tar.gz  
RUN mkdir /opt/tomcat  
RUN tar xvf apache-tomcat-7*tar.gz -C /opt/tomcat --strip-components=1  
ENV CATALINA_HOME=/opt/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
# Modify these options as needed  
ENV JAVA_OPTS="-Djava.awt.headless=true
-Djava.security.egd=file:/dev/./urandom"  
ENV CATALINA_OPTS="-Xms2096m -Xmx4096m -XX:+UseConcMarkSweepGC
-XX:+UseParNewGC -XX:+AlwaysPreTouch -XX:+DisableExplicitGC"  
  
EXPOSE 8080  
  
###############################################################################  
# hybris  
###############################################################################  
  
RUN mkdir -p /datahub/war  
RUN cp /hybris/hybris/bin/ext-integration/datahub/web-app/datahub-
webapp-5.7.0.0-RC5.war /datahub/war  
  
RUN mkdir -p /datahub/config  
ADD config/local.properties /datahub/config/local.properties  
  
RUN mkdir -p /datahub/extensions  
RUN cp /hybris/hybris/bin/ext-integration/datahub/extensions/sap/*.jar
/datahub/extensions  
ADD extensions/*.jar /datahub/extensions/  
  
# Required as of 5.7.0.0  
RUN rm /datahub/extensions/sapproductconfiguration-5.7.0.0-RC15.jar  
  
ADD datahub-webapp.xml /opt/tomcat/conf/Catalina/localhost/  
  
#copy mysql connector jar to tomcat lib  
ADD ./libs /opt/tomcat/lib  
  
#RUN rm -rf /hybris  
  
###############################################################################  
# Start  
###############################################################################  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD [ "/start.sh" ]  

