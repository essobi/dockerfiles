FROM nidupont/debian-oracle-java  
  
MAINTAINER Nicolas Dupont <nidupont@gmail.com>  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.73  
ENV JAVA_HOME /opt/jalios/instances/jvm/jdk7  
  
ENV CATALINA_HOME /opt/jalios/instances/server/tomcat${TOMCAT_MAJOR}  
ENV CATALINA_BASE /opt/jalios/apps/apache-tomcat-base/jplatform  
  
ENV PATH $CATALINA_BASE/bin:$CATALINA_HOME/bin:$PATH  
  
WORKDIR $CATALINA_BASE  
  
# System update and packages installation  
RUN apt-get update -q && \  
apt-get install -q -y --no-install-recommends wget unzip  
  
# Tomcat 7 installation  
RUN wget
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /opt/jalios/downloads/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
mkdir -p /opt/jalios/components/apache-tomcat && \  
tar -xvf /opt/jalios/downloads/apache-tomcat-${TOMCAT_VERSION}.tar.gz -C
/opt/jalios/components/apache-tomcat && \  
rm -rf /opt/jalios/components/apache-tomcat/apache-
tomcat-${TOMCAT_VERSION}/webapps/* && \  
mkdir -p /opt/jalios/instances/server && \  
ln -s /opt/jalios/components/apache-tomcat/apache-tomcat-${TOMCAT_VERSION}
${CATALINA_HOME} && \  
mkdir -p \  
${CATALINA_BASE}/bin \  
${CATALINA_BASE}/conf \  
${CATALINA_BASE}/webapps \  
${CATALINA_BASE}/logs \  
${CATALINA_BASE}/temp \  
${CATALINA_BASE}/work && \  
cp ${CATALINA_HOME}/conf/tomcat-users.xml ${CATALINA_BASE}/conf/ && \  
cp ${CATALINA_HOME}/conf/logging.properties ${CATALINA_BASE}/conf/  
  
COPY setenv.sh ${CATALINA_BASE}/bin/  
RUN chmod +x ${CATALINA_BASE}/bin/*.sh  
  
# Configuration tuning for JPlatform  
RUN sed -e "s/<Context>/<Context useHttpOnly=\"true\" allowLinking=\"true\"
>/g" <${CATALINA_HOME}/conf/context.xml >${CATALINA_BASE}/conf/context.xml &&
\  
sed -e "s/<Connector/<Connector URIEncoding=\"UTF-8\"/g"
<${CATALINA_HOME}/conf/server.xml >${CATALINA_BASE}/conf/server.xml && \  
sed -e "s/<servlet-class>org.apache.jasper.servlet.JspServlet<\/servlet-
class>/<servlet-class>org.apache.jasper.servlet.JspServlet<\/servlet-
class>\n\t<init-param>\n\t\t<param-name>development<\/param-name>\n\t\t<param-
value>false<\/param-value>\n\t<\/init-param>/g" <${CATALINA_HOME}/conf/web.xml
>${CATALINA_BASE}/conf/web.xml  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

