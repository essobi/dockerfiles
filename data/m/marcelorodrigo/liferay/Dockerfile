FROM java:8-alpine  
MAINTAINER Marcelo Rodrigo <mrodrigow@gmail.com>  
  
RUN apk add --no-cache curl unzip  
RUN curl -O -k -L
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.2%20GA3/liferay-
ce-portal-tomcat-7.0-ga3-20160804222206210.zip \  
&& unzip liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip -d /opt \  
&& rm liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip  
RUN ln -s /opt/liferay-ce-portal-7.0-ga3 /opt/liferay \  
&& ln -s /opt/liferay/tomcat-8.0.32 /opt/liferay/tomcat  
RUN echo -e '\nCATALINA_OPTS="$CATALINA_OPTS
-Djava.security.egd=file:/dev/./urandom"' >> /opt/liferay/tomcat/bin/setenv.sh  
  
VOLUME ["/opt/liferay"]  
EXPOSE 8080  
CMD /opt/liferay/tomcat/bin/catalina.sh run && tail -f
/opt/liferay/tomcat/logs/catalina.out  

