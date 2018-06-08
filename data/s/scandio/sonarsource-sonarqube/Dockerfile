FROM sonarqube:5.6  
MAINTAINER Scandio GmbH  
  
ENV SONARQUBE_HOME /opt/sonarqube  
  
# Expose HTTP port  
EXPOSE 9000  
ENV JDBC_URL
jdbc:mysql://db/sonarqube?autoReconnect=true&characterEncoding=utf8&useUnicode=true&rewriteBatchedStatements=true&useConfigs=maxPerformance  
ENV JDBC_USERNAME sonarqube  
ENV JDBC_PASSWORD sonarqube  
ENV HTTP_PROXYHOST false  
ENV HTTP_PROXYPORT false  
ENV HTTP_PROXYUSER false  
ENV HTTP_PROXYPASSWORD false  
  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
VOLUME ["${SONARQUBE_HOME}/data", "${SONARQUBE_HOME}/extensions",
"${SONARQUBE_HOME}/conf"]  
  
WORKDIR ${SONARQUBE_HOME}  
RUN mkdir ${SONARQUBE_HOME}/conftemplate && \  
cp ${SONARQUBE_HOME}/conf/sonar.properties ${SONARQUBE_HOME}/conftemplate/ &&
\  
cp ${SONARQUBE_HOME}/conf/wrapper.conf ${SONARQUBE_HOME}/conftemplate/  
COPY configure-and-start.sh ${SONARQUBE_HOME}/bin/  
RUN chmod +x ${SONARQUBE_HOME}/bin/configure-and-start.sh  
ENTRYPOINT ["./bin/configure-and-start.sh"]  
  

