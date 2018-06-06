FROM tomcat:7.0  
MAINTAINER Jedrzej Rybicki  
ADD supervisord.conf /etc/supervisord.conf  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install
supervisor -y && \  
apt-get clean autoclean && apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
EXPOSE 8080  
RUN wget -q -O '/tmp/voyant.zip' 'http://dev.voyant-
tools.org/downloads/current/VoyantServer.zip' && \  
mkdir /tmp/voyant/ && cd /tmp/voyant/ && unzip -qq /tmp/voyant.zip && \  
rm -rf /usr/local/tomcat/webapps/ROOT/ && cp -r _app/
/usr/local/tomcat/webapps/ROOT/ && \  
cd /usr/local/tomcat/ && rm -rf /tmp/voyant.zip /tmp/voyant/  
VOLUME /usr/local/tomcat/temp  
CMD supervisord -c /etc/supervisord.conf  

