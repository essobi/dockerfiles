# rstuven/wso2-ids  
FROM justinwalsh/centos-jre7  
  
MAINTAINER Ricardo Stuven  
  
RUN wget -P /opt http://product-dist.wso2.com/downloads/identity-
server/5.0.0/wso2is-5.0.0.zip && \  
unzip /opt/wso2is-5.0.0.zip -d /opt && \  
mv /opt/wso2is-5.0.0 /opt/wso2 && \  
rm /opt/wso2is-5.0.0.zip  
  
WORKDIR /opt/wso2/  
  
EXPOSE 9443  
CMD ["/opt/wso2/bin/wso2server.sh"]  

