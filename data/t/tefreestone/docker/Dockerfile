FROM fedora  
  
MAINTAINER Tom Freestone <tfreestone@ldschurch.org>  
#RUN yum update  
RUN yum install -y wget tar gzip  
  
ENV JAVA_HOME /opt/jdk/jre  
ENV PATH $PATH:/opt/jdk/jre/bin  
ENV OPENAM_DIR /opt/openam  
  
RUN wget --no-check-certificate -O /tmp/pkg.tar.gz --header "Cookie:
oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz && \  
tar -zxf /tmp/pkg.tar.gz --xform='s/[^\/]*/jdk/' -C /opt && \  
rm -rf /tmp/*  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
RUN mkdir -p "$OPENAM_DIR"  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.62  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
ENV PASS 1dumbPassword  
RUN set -x \  
&& wget "$TOMCAT_TGZ_URL" -O /tmp/tomcat.tar.gz \  
&& cd ${CATALINA_HOME}/;tar -zxvf /tmp/tomcat.tar.gz --strip-components=1 \  
&& rm /tmp/tomcat.tar.gz*  
RUN sed -i -r 's/<\/tomcat-users>//' ${CATALINA_HOME}/conf/tomcat-users.xml  
RUN echo '<role rolename="manager-gui"/>' >> ${CATALINA_HOME}/conf/tomcat-
users.xml  
RUN echo '<role rolename="manager-script"/>' >> ${CATALINA_HOME}/conf/tomcat-
users.xml  
RUN echo '<role rolename="manager-jmx"/>' >> ${CATALINA_HOME}/conf/tomcat-
users.xml  
RUN echo '<role rolename="admin-gui"/>' >> ${CATALINA_HOME}/conf/tomcat-
users.xml  
RUN echo '<role rolename="admin-script"/>' >> ${CATALINA_HOME}/conf/tomcat-
users.xml  
RUN echo "<user username=\"admin\" password=\"${PASS}\" roles=\"manager-
gui,manager-script,manager-jmx,admin-gui, admin-script\"/>" >>
${CATALINA_HOME}/conf/tomcat-users.xml  
RUN echo '</tomcat-users>' >> ${CATALINA_HOME}/conf/tomcat-users.xml  
RUN rm -rf /opt/tomcat/webapps/examples && rm -rf /opt/tomcat/webapps/docs  
  
RUN echo '#! /bin/sh' >${CATALINA_HOME}/bin/setenv.sh  
RUN echo 'export JAVA_OPTS="$CATALINA_OPTS -Xms64m -Xms64m -Xmx512m
-XX:+UseG1GC -XX:MaxPermSize=256m
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005" ' >>
${CATALINA_HOME}/bin/setenv.sh  
  
RUN sed -i "s#</Server>##g" /opt/tomcat//conf/server.xml; \  
sed -i "s# </Service>##g" /opt/tomcat/conf/server.xml; \  
echo ' <Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"
maxThreads="150" scheme="https" secure="true" clientAuth="false"
sslProtocol="TLS" keystoreFile="/opt/tomcat/.keystore"
keystorePass="tomcat_admin" />' >> ${CATALINA_HOME}/conf/server.xml; \  
echo ' </Service>' >> /opt/tomcat/conf/server.xml; \  
echo '</Server>' >>/opt/tomcat/conf/server.xml  
  
RUN printf
tomcat_admin\\\ntomcat_admin\\\n\\\n\\\n\\\n\\\n\\\n\\\ny\\\ntomcat_admin\\\ntomcat_admin\\\n
| keytool -genkey -alias tomcat -keyalg RSA -keystore /opt/tomcat/.keystore;  
  
VOLUME /OPENAM  
EXPOSE 8080  
EXPOSE 8443  
EXPOSE 50389  
EXPOSE 5005  
ENV OPENAM_WAR
https://code.ldschurch.org/nexus/service/local/repo_groups/main-
repo/content/org/lds/ics/openAM/openAM/2.0.2/openAM-2.0.2.war  
RUN set -x \  
&& wget "$OPENAM_WAR" -O /opt/tomcat/webapps/sso.war  
WORKDIR $CATALINA_HOME  
CMD /opt/tomcat/bin/catalina.sh run  
  

