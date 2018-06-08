# Liferay 6.2  
#  
# VERSION 0.0.1  
# Fork from snasello/docker-liferay-6.2  
# 0.0.1 : initial static setup for mysql & liferay multi-tier example  
FROM snasello/docker-debian-java7:7u71  
  
MAINTAINER Robert Szymczak <rszymczak@fum.de>  
  
# install liferay  
RUN apt-get install -y unzip \  
&& curl -O -s -k -L -C -
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.1%20GA2/liferay-
portal-tomcat-6.2-ce-ga2-20140319114139101.zip \  
&& unzip liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip -d /opt \  
&& rm liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip  
  
# add config for mysql database  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-
properties=mysql.properties"' >> /opt/liferay-portal-6.2-ce-
ga2/tomcat-7.0.42/bin/setenv.sh  
  
# add config for liferay  
ADD config/liferay.properties /opt/liferay-portal-6.2-ce-
ga2/liferay.properties  
ADD config/mysql.properties /opt/liferay-portal-6.2-ce-ga2/mysql.properties  
  
# volumes  
VOLUME ["/var/liferay-home", "/opt/liferay-portal-6.2-ce-ga2/"]  
  
# Ports  
EXPOSE 8080  
# Set JAVA_HOME  
ENV JAVA_HOME /opt/java  
  
# EXEC  
CMD ["run"]  
ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga2/tomcat-7.0.42/bin/catalina.sh"]  

