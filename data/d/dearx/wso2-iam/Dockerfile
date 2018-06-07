FROM dearx/env-java8:latest  
  
#ARG VCS_REF  
#LABEL org.label-schema.vcs-ref=$VCS_REF \  
# org.label-schema.vcs-url="https://github.com/ihcsim/docker-wso2apim"  
  
ARG VERSION=${VERSION:-5.3.0}  
RUN wget -P /opt https://storage.googleapis.com/esitolo-
apps/wso2/wso2is-${VERSION}.zip && \  
apt-get update && \  
apt-get install -y zip && \  
apt-get clean && \  
unzip /opt/wso2is-${VERSION}.zip -d /opt && \  
rm /opt/wso2is-${VERSION}.zip  
  
#ADD carbon.xml /opt/wso2is-${VERSION}/repository/conf/  
#ADD web.xml /opt/wso2is-${VERSION}/repository/conf/tomcat/carbon/WEB-INF/  
  
EXPOSE 8000 9763 9443 10500  
WORKDIR /opt/wso2is-${VERSION}  
ENTRYPOINT ["bin/wso2server.sh"]

