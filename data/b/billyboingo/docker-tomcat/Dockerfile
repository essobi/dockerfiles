FROM billyboingo/docker-oracle-jdk:java8  
MAINTAINER Bill Weiss <billyboingo@gmail.com>  
  
#Install the tools we will need  
RUN apt-get -q update && apt-get install -qy --force-yes \  
wget \  
unzip  
  
ENV SERVER_DIR /app  
ENV WEBAPPS_DIR $SERVER_DIR/webapps  
  
ENV CATALINA_HOME $SERVER_DIR  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.23  
ENV TOMCAT_URL
http://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.zip  
  
#Download and install latest Tomcat  
RUN export TOMCAT_FILE=$(echo $TOMCAT_URL | awk -F"/bin/" '{print $2}') && \  
export TOMCAT_DIR=$(echo $TOMCAT_FILE | sed 's/.zip//g') && \  
wget -nv -P /tmp $TOMCAT_URL && \  
unzip /tmp/$TOMCAT_FILE -d /tmp && \  
mv /tmp/$TOMCAT_DIR/* $SERVER_DIR && \  
chmod u+x $SERVER_DIR/bin/catalina.sh  
  
#Adding Custom files  
COPY services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
  
#Setup locale  
RUN locale-gen en_US && \  
locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
#Clean up  
RUN apt-get -y autoremove; apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* $SERVER_DIR/bin/*.bat $WEBAPPS_DIR/*  
  
EXPOSE 8080

