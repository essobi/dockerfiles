FROM openjdk:8-jre  
MAINTAINER Andres Chavez <aschavezu@gmail.com>  
  
RUN wget http://www2.sunat.gob.pe/facturador/Jetty_version_1.0.4.zip && \  
unzip Jetty_version_*.zip && \  
rm Jetty_version_*.zip && \  
chmod a+x /Jetty/iniciarSistema.bat  
RUN wget http://www2.sunat.gob.pe/facturador/data0_version_1.0.4.zip && \  
unzip data0_version_*.zip && \  
rm data0_version_*.zip  
  
WORKDIR /Jetty  
  
EXPOSE 8090  
  
CMD java -Dfile.encoding=ISO8859_1 -Duser.country=US -Duser.language=en
-Djavax.net.debug=all -jar start.jar  

