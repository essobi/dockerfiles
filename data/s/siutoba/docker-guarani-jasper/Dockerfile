FROM debian:jessie  
MAINTAINER ablanco@siu.edu.ar  
  
# Se instala java para jasper  
RUN echo "deb http://http.us.debian.org/debian jessie main contrib" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends openjdk-7-jre-headless \  
&& apt-get install -y --reinstall ttf-mscorefonts-installer \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD java -jar /var/local/gestion/lib/toba/php/3ros/JavaBridge/WEB-
INF/lib/JavaBridge.jar SERVLET:8081  

