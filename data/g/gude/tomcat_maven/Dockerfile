FROM maven:3.3.3  
MAINTAINER Guodong  
ADD settings.xml /home/  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_VERSION 8.0.33  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& mv /home/settings.xml /usr/share/maven/conf/settings.xml \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

