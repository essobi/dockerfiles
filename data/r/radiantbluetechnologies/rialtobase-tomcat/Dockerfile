# radiantbluetechnologies/rialtobase-tomcat  
FROM radiantbluetechnologies/rialtobase-java  
MAINTAINER mpg@flaxen.com  
  
# Prepare environment  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin:$CATALINA_HOME/scripts  
  
# Install Tomcat  
RUN wget http://apache-
mirror.rbc.ru/pub/apache/tomcat/tomcat-8/v8.0.24/bin/apache-
tomcat-8.0.24.tar.gz && \  
tar -xvf apache-tomcat-8.0.24.tar.gz && \  
rm apache-tomcat*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME}  
  
RUN chmod +x ${CATALINA_HOME}/bin/*sh  
  
# Create Tomcat admin user  
###ADD create_admin_user.sh $CATALINA_HOME/scripts/create_admin_user.sh  
###ADD tomcat.sh $CATALINA_HOME/scripts/tomcat.sh  
###RUN chmod +x $CATALINA_HOME/scripts/*.sh  
# Create tomcat user  
###RUN groupadd -r tomcat && \  
### useradd -g tomcat -d ${CATALINA_HOME} -s /sbin/nologin -c "Tomcat user"
tomcat && \  
### chown -R tomcat:tomcat ${CATALINA_HOME}  
WORKDIR /opt/tomcat  
  
EXPOSE 8080  
EXPOSE 8009  
###USER tomcat  
CMD ["tomcat.sh"]  

