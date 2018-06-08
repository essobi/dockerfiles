FROM tomcat:8.0  
MAINTAINER Lucas Souza <lucassampsouza@gmail.com>  
  
ENV TZ="GMT"  
ENV APEX_CONFIG_DIR="/opt"  
ENV TOMCAT_HOME="/usr/local/tomcat"  
ENV DATABASE_PUBLIC_USERNAME="APEX_PUBLIC_USER"  
ENV CONFIGURE_APEX="true"  
ENV CONFIGURE_APEX_REST="true"  
ENV CONFIGURE_ORDS="true"  
ADD i.tar.bz2 $TOMCAT_HOME/webapps  
COPY ords.war $TOMCAT_HOME/webapps/  
RUN chmod 755 $TOMCAT_HOME/webapps/i  
RUN chown -R root:root $TOMCAT_HOME/webapps/i  
  
RUN java -jar $TOMCAT_HOME/webapps/ords.war configdir $APEX_CONFIG_DIR  
  
COPY ./config_ords_and_run_catalina.sh /  
RUN chmod +x /config_ords_and_run_catalina.sh  
  
ENTRYPOINT ["/config_ords_and_run_catalina.sh"]  
VOLUME ["/opt"]  
  
EXPOSE 8080  
CMD ["run"]  

