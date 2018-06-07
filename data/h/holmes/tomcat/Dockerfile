FROM holmes/java:1.7.0_71  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r tomcat && useradd -r --create-home -g tomcat tomcat  
RUN yum install -y tar  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
RUN mkdir -p "$CATALINA_HOME" && chown tomcat:tomcat "$CATALINA_HOME"  
  
WORKDIR $CATALINA_HOME  
  
USER tomcat  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.57  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN curl -SL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
COPY ./server.xml /usr/local/tomcat/conf/server.xml  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

