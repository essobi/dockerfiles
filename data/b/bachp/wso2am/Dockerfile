#  
# WSO2 API Manager  
#  
FROM openjdk:8  
MAINTAINER Ivan Sim, ihcsim@gmail.com  
  
ENV VERSION 2.0.0  
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
  
VOLUME ["/opt/wso2am/repository"]  
  
EXPOSE 9443 9763 8243 8280 10397 7711  
ENTRYPOINT ["/opt/wso2am/bin/wso2server.sh"]  

