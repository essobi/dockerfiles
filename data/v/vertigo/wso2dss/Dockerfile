FROM anapsix/alpine-java:jdk8  
MAINTAINER Raphael Bottino <rbottino@vertigo.com.br>  
  
# Install wget and unzip  
RUN apk update && apk add wget unzip  
  
# Download and extract wso2dss-3.5.0  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" -O
/tmp/wso2dss-3.5.0.zip http://product-dist.wso2.com/products/data-services-
server/3.5.0/wso2dss-3.5.0.zip && \  
unzip /tmp/wso2dss-3.5.0.zip -d /opt && \  
rm -f /tmp/wso2dss-3.5.0.zip  
  
# Creates a default place to deploy carbonapps  
RUN ln -s /carbonapps
/opt/wso2dss-3.5.0/repository/deployment/server/carbonapps  
  
# Exporting ports  
EXPOSE 9443  
#Running DSS  
CMD ["/opt/wso2dss-3.5.0/bin/wso2server.sh"]

