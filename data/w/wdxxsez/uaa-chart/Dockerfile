FROM tomcat:8.0-jre8-alpine  
  
ENV UAA_VERSION 4.11.0  
RUN apk update && \  
apk add --no-cache openssl && \  
rm -rf /var/cache/apk/*  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
  
ADD http://central.maven.org/maven2/org/cloudfoundry/identity/cloudfoundry-
identity-uaa/${UAA_VERSION}/cloudfoundry-identity-uaa-${UAA_VERSION}.war
/usr/local/tomcat/webapps/ROOT.war  
  
RUN mkdir -p /usr/local/uaa/bin && mkdir -p /usr/local/uaa/config  
  
COPY config/* /usr/local/uaa/config/  
  
COPY bin/* /usr/local/uaa/bin/  
  
RUN chmod -R +x /usr/local/uaa/bin/*  
  
EXPOSE 8080  
CMD ["/usr/local/uaa/bin/run.sh"]  

