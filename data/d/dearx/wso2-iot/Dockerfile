FROM dearx/env-java8:latest  
  
#ARG VCS_REF  
#LABEL org.label-schema.vcs-ref=$VCS_REF \  
# org.label-schema.vcs-url="https://github.com/ihcsim/docker-wso2apim"  
ARG VERSION=${VERSION:-3.0.0}  
RUN wget -P /opt https://storage.googleapis.com/esitolo-
apps/wso2/wso2iot-${VERSION}.zip && \  
apt-get update && \  
apt-get install -y zip maven && \  
apt-get clean && \  
unzip /opt/wso2iot-${VERSION}.zip -d /opt && \  
rm /opt/wso2iot-${VERSION}.zip  
  
#ADD carbon.xml /opt/wso2is-${VERSION}/repository/conf/  
#ADD web.xml /opt/wso2is-${VERSION}/repository/conf/tomcat/carbon/WEB-INF/  
EXPOSE 9446 9445 9443  
WORKDIR /opt/wso2iot-${VERSION}  
RUN mvn clean install -f ./plugins/plugins-deployer.xml  
ENTRYPOINT ["core/bin/wso2server.sh"]

