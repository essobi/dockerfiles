FROM tomcat:7-jre7  
MAINTAINER Chris Montes <chris@sapho.com>  
  
ENV SAPHO_VERSION 2.2.2  
ENV RDS_DB_NAME ebdb  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
WORKDIR /root  
  
COPY launch.sh ${CATALINA_HOME}/bin/  
  
RUN chmod +x ${CATALINA_HOME}/bin/launch.sh  
EXPOSE 8080  
CMD ["launch.sh"]  

