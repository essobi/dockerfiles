FROM debian:jessie  
MAINTAINER ablanco@siu.edu.ar  
  
# Se instala java para jasper  
RUN echo "deb http://http.us.debian.org/debian jessie main contrib" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends openjdk-7-jre-headless \  
&& apt-get install -y --reinstall ttf-mscorefonts-installer \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD java -cp
'/var/local/jasper/JasperReports/*:/var/local/jasper/JavaBridge/WEB-INF/lib/*'
php.java.bridge.Standalone SERVLET:8081  

