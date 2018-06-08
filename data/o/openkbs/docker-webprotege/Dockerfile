FROM openkbs/jre-tomcat  
  
MAINTAINER DrSnowbird <DrSnowbird@openkbs.org>  
  
ENV WEBPROTEGE_VERSION="2.6.0"  
ENV JAVA_OPTS="$JAVA_OPTS -Dfile.encoding=UTF-8"  
ENV CATALINA_HOME=${CATALINA_HOME:-/tomcat}  
  
ENV WEBPROTEGE_DATA=/data/webprotege  
ENV CATALINA_WEBAPPS=${CATALINA_HOME}/webapps  
ENV INSTALL_DIR=${CATALINA_WEBAPPS}/ROOT  
  
#TARGET_URL=https://github.com/protegeproject/webprotege/releases/download/v2.6.0/webprotege-2.6.0.war  
ENV
TARGET_URL=https://github.com/protegeproject/webprotege/releases/download/v${WEBPROTEGE_VERSION}/webprotege-${WEBPROTEGE_VERSION}.war  
  
WORKDIR ${CATALINA_WEBAPPS}  
  
RUN echo ${CATALINA_HOME} \  
&& mkdir -p ${WEBPROTEGE_DATA} \  
&& cp -r ROOT ROOT.save \  
&& rm -rf ROOT/* \  
# && wget -q -O webprotege.war
https://github.com/protegeproject/webprotege/releases/download/v${WEBPROTEGE_VERSION}/webprotege-${WEBPROTEGE_VERSION}.war
\  
&& wget -q -O webprotege.war ${TARGET_URL} \  
&& unzip -q webprotege.war -d ${CATALINA_WEBAPPS}/ROOT \  
&& rm webprotege.war \  
&& sed -i 's/#mongodb.host=localhost/mongodb.host=mongodb/g'
${CATALINA_WEBAPPS}/ROOT/WEB-INF/classes/webprotege.properties  
  
COPY config/webprotege.properties
${CATALINA_WEBAPPS}/ROOT/webprotege.properties  
  
VOLUME ${WEBPROTEGE_DATA}  
VOLUME ${CATALINA_WEBAPPS}  
  
EXPOSE 8080  
#CMD ["catalina.sh", "run"]  
CMD ["/entry.sh", "run"]  

