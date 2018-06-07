FROM debian:jessie  
MAINTAINER estebanv@unlu.edu.ar  
  
RUN echo "deb http://http.us.debian.org/debian jessie main contrib" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends openjdk-7-jre-headless \  
&& apt-get install -y --reinstall ttf-mscorefonts-installer \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8081  
# La variable que contiene el path del bridge. por lo general se baja a la
carpeta de terceros de Toba  
CMD java -jar $PATH_BRIDGE\JavaBridge.jar SERVLET:8081  

