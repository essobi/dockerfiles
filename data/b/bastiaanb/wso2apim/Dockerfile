#  
# WSO2 API Manager 1.9.0  
#  
FROM java:7  
MAINTAINER Bastiaan Bakker, bastiaan@nakednerds.net  
  
# download and install WSO2 API manager  
RUN wget -P /opt --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" \  
http://product-dist.wso2.com/products/api-manager/1.9.0/wso2am-1.9.0.zip && \  
echo 93d26464f607a14e70d75f19f57bc465c9be4f12e56829e03571c6ad99da3086
/opt/wso2am-1.9.0.zip | sha256sum -c --quiet && \  
apt-get update && \  
apt-get install -y zip ant && \  
apt-get clean && \  
unzip /opt/wso2am-1.9.0.zip -d /opt && \  
rm /opt/wso2am-1.9.0.zip  
  
# add import export tool  
RUN wget -P /opt/wso2am-1.9.0/repository/deployment/server/webapps
'https://docs.wso2.com/download/attachments/45971876/api-import-
export-v0.9.1.war?version=1&modificationDate=1439462301000&api=v2'  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
EXPOSE 9443 9763 8280 8243  
CMD ["/opt/wso2am-1.9.0/bin/wso2server.sh"]  

