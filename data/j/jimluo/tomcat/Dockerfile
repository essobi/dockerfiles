FROM microimages/jre  
  
LABEL service=tomcat  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.73  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN wget "$TOMCAT_TGZ_URL" -O /tmp/tomcat.tar.gz \  
&& cd $CATALINA_HOME && tar zxf /tmp/tomcat.tar.gz \  
&& mv apache-tomcat-$TOMCAT_VERSION/* ./ && rmdir apache-
tomcat-$TOMCAT_VERSION \  
&& rm bin/*.bat \  
&& mv webapps/* /app/ && rmdir webapps && ln -s /app webapps \  
&& rm /tmp/tomcat.tar.gz  
  
WORKDIR /app  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

