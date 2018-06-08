FROM openjdk:8  
ENV CATALINA_HOME /usr/local/tomcat  
  
RUN apt-get -y update && \  
apt-get -y install libreoffice imagemagick swftools liblog4j1.2-java
libgnumail-java ant curl unzip sudo tar libreoffice-common  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN curl -L
https://jaist.dl.sourceforge.net/project/openkm/6.3.2/openkm-6.3.2-community-
tomcat-bundle.zip -o /usr/local/openkm.zip && \  
unzip /usr/local/openkm.zip -d /usr/local/ && \  
rm /usr/local/openkm.zip && \  
ln -s $CATALINA_HOME /opt/openkm  
  
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
VOLUME /opt/openkm/repository  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080 2002  

