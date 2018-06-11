FROM openjdk:8u111-jre  
  
MAINTAINER Medve Zoltan <debugmedve@gmail.com>  
  
ENV WILDFLY_RELEASE_DATE="2016-01-29"  
ENV WILDFLY_VERSION="10.0.0.Final"  
ENV
WILDFLY_URL="https://download.jboss.org/wildfly/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz"  
ENV WILDFLY_HOME="/opt/wildfly"  
ENV PATH="${WILDFLY_HOME}/bin:$PATH"  
WORKDIR ${WILDFLY_HOME}  
RUN curl ${WILDFLY_URL} | tar -xz --strip 1 && \  
sed -i -e "s/<inet.*/<any-address\/>/"
${WILDFLY_HOME}/standalone/configuration/standalone.xml  
  
VOLUME /opt/wildfly/standalone/deployments  
VOLUME /opt/wildfly/standalone/modules  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]  
  
#HTTP  
EXPOSE 8080  
#HTTPS  
EXPOSE 8443  
#HTTP MANAGEMENT  
EXPOSE 9990  
#HTTPS MANAGEMENT  
EXPOSE 9993  
#AJP  
EXPOSE 8009  
#TXN RECOVERY  
EXPOSE 4712  
#TXN STATUS MANAGER  
EXPOSE 4713  
CMD ["standalone"]  
  

