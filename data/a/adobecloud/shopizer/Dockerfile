FROM google/debian:wheezy  
  
MAINTAINER dharmi@gmail.com  
  
# Install JDK with no add-ons  
RUN apt-get update && \  
apt-get -y -f install --no-install-recommends openjdk-7-jdk && \  
apt-get -y -f install curl  
  
#Install Tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.63  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf /usr/local/tomcat/webapps/examples \  
&& rm -rf /usr/local/tomcat/webapps/docs \  
&& rm -rf /usr/local/tomcat/webapps/ROOT \  
&& chmod -R 777 /usr/local/tomcat  
  
#HTTP port  
EXPOSE 8080  
ADD shopizer.war webapps/ROOT.war  
  
# Start Tomcat  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]

