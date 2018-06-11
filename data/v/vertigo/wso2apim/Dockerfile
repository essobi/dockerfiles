FROM anapsix/alpine-java:jdk8  
MAINTAINER Raphael Bottino <rbottino@vertigo.com.br>  
  
# Install wget and unzip  
RUN apk update && apk add wget unzip  
  
# Download and extract wso2am-1.10.0  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" -O
/tmp/wso2am-1.10.0.zip http://product-dist.wso2.com/products/api-
manager/1.10.0/wso2am-1.10.0.zip && \  
unzip /tmp/wso2am-1.10.0.zip -d /opt && \  
rm -f /tmp/wso2am-1.10.0.zip  
  
# Creates a default place to deploy carbonapps  
RUN ln -s /carbonapps
/opt/wso2am-1.10.0/repository/deployment/server/carbonapps  
  
# Exporting ports  
EXPOSE 9443  
EXPOSE 9763  
EXPOSE 10389  
EXPOSE 8000  
EXPOSE 10397  
EXPOSE 8243  
EXPOSE 8280  
EXPOSE 7711  
#Running APIM  
CMD ["/opt/wso2am-1.10.0/bin/wso2server.sh"]

