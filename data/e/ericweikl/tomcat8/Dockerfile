FROM jeanblanchard/busybox-java:jdk8  
  
MAINTAINER Eric Weikl <eric.weikl@gmx.net>  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION ${TOMCAT_MAJOR}.0.9  
ENV CATALINA_HOME /opt/tomcat  
ENV BASE_URI http://archive.apache.org/dist/tomcat  
ENV DOWNLOAD_URI
${BASE_URI}/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
  
RUN mkdir -p $(dirname ${CATALINA_HOME}) \  
&& curl --silent ${DOWNLOAD_URI} | gunzip -c | tar xf - -C /tmp \  
&& mv /tmp/apache-tomcat* ${CATALINA_HOME} \  
&& rm -rf ${CATALINA_HOME}/webapps/examples ${CATALINA_HOME}/webapps/docs  
  
ADD tomcat-users.xml ${CATALINA_HOME}/conf/  
ADD deploy-and-run.sh ${CATALINA_HOME}/bin/  
  
RUN adduser -D -u 431 -H -h ${CATALINA_HOME} -s /bin/nologin tomcat \  
&& chown -R tomcat:tomcat ${CATALINA_HOME} \  
&& chmod 755 ${CATALINA_HOME}/bin/deploy-and-run.sh  
  
USER tomcat  
  
ENV HOME /opt/tomcat  
EXPOSE 8080  
CMD ${CATALINA_HOME}/bin/deploy-and-run.sh  

