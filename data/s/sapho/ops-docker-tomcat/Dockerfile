FROM tomcat:8-jre8  
MAINTAINER Chris Montes <chris@sapho.com>  
  
ENV SAPHO_VERSION 4.8.3  
ENV SAPHO_DB_HOSTNAME mysql  
ENV SAPHO_DB_PASSWORD p244w0rd  
ENV SAPHO_DB_PORT 3306  
ENV SAPHO_DB_TYPE mysql  
ENV SAPHO_DB_NAME sapho  
ENV SAPHO_DB_USERNAME root  
ENV SAPHO_MEMORY_LIMIT 2g  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
WORKDIR /root  
  
COPY launch.sh ${CATALINA_HOME}/bin/  
  
RUN apt-get update && \  
echo GMT > /etc/timezone && \  
chmod +x ${CATALINA_HOME}/bin/launch.sh && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /${CATALINA_HOME}/webapps/ROOT && rm -rf
/${CATALINA_HOME}/webapps/docs  
RUN rm -rf /${CATALINA_HOME}/webapps/examples && rm -rf
/${CATALINA_HOME}/webapps/host-manager  
RUN rm -rf /${CATALINA_HOME}/webapps/manager  
  
RUN wget -q https://s3-us-
west-1.amazonaws.com/download.sapho.com/sapho-4.8.3.zip -O sapho-latest.zip  
  
CMD ["launch.sh"]

