FROM pablotech/hedge-j2se:latest  
# https://github.com/docker-library/tomcat/blob/master/9.0/jre8/Dockerfile  
# TODO: add Tomcat!  
RUN apt-get -y install tomcat7 tomcat7-admin tomcat7-common tomcat7-docs
tomcat7-examples tomcat7-user  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/default/tomcat7  
RUN echo "CATALINA_HOME=/usr/share/tomcat7/" >> /etc/default/tomcat7  
RUN echo "CATALINA_BASE=/etc/tomcat7/Catalina/" >> /etc/default/tomcat7  
  
RUN sed -i -r 's/<\/tomcat-users>//' /etc/tomcat7/tomcat-users.xml  
RUN echo " <role rolename=\"manager-gui\"/>" >> /etc/tomcat7/tomcat-users.xml  
RUN echo " <role rolename=\"admin-gui\"/>" >> /etc/tomcat7/tomcat-users.xml  
RUN echo " <user username=\"admin\" password=\"admin\" roles=\"manager-
gui,admin-gui\"/>" >> /etc/tomcat7/tomcat-users.xml  
RUN echo "</tomcat-users>" >> /etc/tomcat7/tomcat-users.xml  
  
RUN mkdir -p /usr/share/tomcat7/logs/  
RUN mkdir -p /usr/share/tomcat7/temp/  
RUN ln -s /etc/tomcat7/ /usr/share/tomcat7/conf  
RUN chown tomcat7: -R /var/lib/tomcat7/*  
RUN sed -i '/exit 0/c\\\n' /etc/rc.local  
  
EXPOSE 8080/tcp 8009/tcp  
  
  

