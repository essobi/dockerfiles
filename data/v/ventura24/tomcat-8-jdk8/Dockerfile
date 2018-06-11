FROM ventura24/java-8-oracle  
MAINTAINER ventura24  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.36  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& wget ${TOMCAT_TGZ_URL} -O tomcat.tar.gz \  
&& wget ${TOMCAT_TGZ_URL}.asc -O tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

