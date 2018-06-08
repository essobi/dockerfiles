# rstuven/wso2-apim  
FROM chen369/wso2-suite:centos  
  
MAINTAINER Chen Chiu  
  
RUN wget -q --no-check-certificate -P /opt
https://www.dropbox.com/s/e9qivlr2e51hx6a/wso2am-2.1.0.zip && \  
unzip /opt/wso2am-2.1.0.zip -d /opt && \  
mv /opt/wso2am-2.1.0.zip /opt/wso2  
  
WORKDIR /opt/wso2/  
  
EXPOSE 9443  
CMD ["/opt/wso2/bin/wso2server.sh"]  

