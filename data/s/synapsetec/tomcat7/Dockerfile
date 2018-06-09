FROM rdemorais/jre8  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_TGZ_URL http://www-
eu.apache.org/dist/tomcat/tomcat-7/v7.0.78/bin/apache-tomcat-7.0.78.tar.gz  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget && \  
wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" && \  
tar -xvf tomcat.tar.gz --strip-components=1 && \  
rm bin/*.bat && \  
rm tomcat.tar.gz* && \  
rm -rf webapps/ROOT && \  
apt-get purge -y --auto-remove wget  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

