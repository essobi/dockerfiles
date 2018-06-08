FROM dockerfile/java  
  
MAINTAINER info@abroweb.ru  
  
ENV TOMCAT_VERSION 6.0.37  
RUN mkdir -p /usr/share/tomcat  
RUN wget --no-verbose -O /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz \  
http://archive.apache.org/dist/tomcat/tomcat-6/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
# stop building if md5sum does not match  
RUN echo "f90b100cf51ae0a444bef5acd7b6edb2 /tmp/apache-
tomcat-$TOMCAT_VERSION.tar.gz" | \  
md5sum -c  
# install tomcat in /usr/share/tomcat  
RUN tar xzf /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz \  
\--strip-components=1 -C /usr/share/tomcat  
ENV CATALINA_HOME /usr/share/tomcat  
  
RUN apt-get install -y unzip  
  
## for dev only  
#ADD ./resources/SpagoBI.war /usr/share/tomcat/webapps/SpagoBI.war  
#ADD ./resources/SpagoBIBirtReportEngine.war
/usr/share/tomcat/webapps/SpagoBIBirtReportEngine.war  
#ADD ./resources/SpagoBIConsoleEngine.war
/usr/share/tomcat/webapps/SpagoBIConsoleEngine.war  
#ADD ./resources/SpagoBIMobileEngine.war
/usr/share/tomcat/webapps/SpagoBIMobileEngine.war  
ADD http://download.forge.ow2.org/spagobi/SpagoBI-bin-4.1.0_01122013.zip
/SpagoBI-bin-4.1.0_01122013.zip  
ADD http://download.forge.ow2.org/spagobi/SpagoBIBirtReportEngine-
bin-4.1.0_01122013.zip /SpagoBIBirtReportEngine-bin-4.1.0_01122013.zip  
ADD http://download.forge.ow2.org/spagobi/SpagoBIConsoleEngine-
bin-4.1.0_01122013.zip /SpagoBIConsoleEngine-bin-4.1.0_01122013.zip  
ADD http://download.forge.ow2.org/spagobi/SpagoBIMobileEngine-
bin-4.1.0_01122013.zip /SpagoBIMobileEngine-bin-4.1.0_01122013.zip  
  
ADD ./resources/conf/server.xml /usr/share/tomcat/conf/server.xml  
## for dev only  
#ADD ./resources/lib/postgresql-9.1-903.jdbc4.jar
/usr/share/tomcat/lib/postgresql-9.1-903.jdbc4.jar  
ADD http://jdbc.postgresql.org/download/postgresql-9.1-903.jdbc4.jar
/usr/share/tomcat/lib/postgresql-9.1-903.jdbc4.jar  
  
ADD ./resources/install /root/install  
RUN chmod 755 /root/install && /root/install  
  
ADD ./resources/conf/SpagoBI/web.xml /usr/share/tomcat/webapps/SpagoBI/WEB-
INF/web.xml  
ADD ./resources/conf/SpagoBIBirtReportEngine/web.xml
/usr/share/tomcat/webapps/SpagoBIBirtReportEngine/WEB-INF/web.xml  
ADD ./resources/conf/SpagoBIConsoleEngine/web.xml
/usr/share/tomcat/webapps/SpagoBIConsoleEngine/WEB-INF/web.xml  
ADD ./resources/conf/SpagoBIMobileEngine/web.xml
/usr/share/tomcat/webapps/SpagoBIMobileEngine/WEB-INF/web.xml  
  
ADD ./resources/SpagobiFilter.jar /usr/share/tomcat/lib/SpagobiFilter.jar  
  
CMD /usr/share/tomcat/bin/startup.sh && tail -F
/usr/share/tomcat/logs/catalina.out  
  
EXPOSE 8080

