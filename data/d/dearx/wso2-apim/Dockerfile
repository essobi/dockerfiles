FROM dearx/env-java8:latest  
  
#ARG VCS_REF  
#LABEL org.label-schema.vcs-ref=$VCS_REF \  
# org.label-schema.vcs-url="https://github.com/ihcsim/docker-wso2apim"  
  
ARG VERSION=${VERSION:-2.1.0}  
RUN wget -P /opt https://storage.googleapis.com/esitolo-
apps/wso2/wso2am-${VERSION}.zip && \  
apt-get update && \  
apt-get install -y zip && \  
apt-get clean && \  
unzip /opt/wso2am-${VERSION}.zip -d /opt && \  
rm /opt/wso2am-${VERSION}.zip  
  
#ADD carbon.xml /opt/wso2am-${APIM_VERSION}/repository/conf/  
#ADD web.xml /opt/wso2am-${APIM_VERSION}/repository/conf/tomcat/carbon/WEB-
INF/  
  
EXPOSE 9443 9763 8243 8280 10397 7711  
WORKDIR /opt/wso2am-${VERSION}  
ENTRYPOINT ["bin/wso2server.sh"]

