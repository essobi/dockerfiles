FROM openjdk:8  
MAINTAINER Sciensa  
  
ENV VERSION 2.1.0  
ENV IP_HOST 127.0.0.1  
RUN wget -P /opt --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"
http://product-dist.wso2.com/products/api-
manager/${VERSION}/wso2am-${VERSION}.zip && \  
apt-get update && \  
apt-get install -y zip && \  
apt-get clean && \  
unzip /opt/wso2am-${VERSION}.zip -d /opt && \  
rm /opt/wso2am-${VERSION}.zip && \  
mv /opt/wso2am-${VERSION} /opt/wso2am  
  
COPY /repository/conf/api-manager.xml /opt/wso2am/repository/conf/api-
manager.xml  
COPY /bin/wso2server.sh /opt/wso2am/bin/wso2server.sh  
  
# Expose WSO2 repository folder to Host  
#VOLUME ["/opt/wso2am/repository"]  
VOLUME ["/opt/wso2am/repository/deployment/server"]  
VOLUME ["/opt/wso2am/repository/components/dropins"]  
VOLUME ["/opt/wso2am/repository/components/lib"]  
VOLUME ["/opt/wso2am/repository/resources/security"]  
VOLUME ["/opt/wso2am/repository/database"]  
VOLUME ["/opt/wso2am/repository/data"]  
VOLUME ["/opt/wso2am/repository/conf"]  
VOLUME ["/opt/wso2am/repository/tenants"]  
VOLUME ["/opt/wso2am/repository/logs"]  
  
WORKDIR /opt/wso2am/bin/  
  
EXPOSE 9443 9763 8243 8280 10397 7711  
ENTRYPOINT ["/opt/wso2am/bin/wso2server.sh"]  

