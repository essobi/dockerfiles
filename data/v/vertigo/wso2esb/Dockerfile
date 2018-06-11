FROM anapsix/alpine-java:jdk8  
MAINTAINER Raphael Bottino <rbottino@vertigo.com.br>  
  
# Install wget and unzip  
RUN apk add --update wget unzip && rm -rf /var/cache/apk/*  
  
# Download and extract wso2esb-4.9.0  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" -O
/tmp/wso2esb-4.9.0.zip http://product-dist.wso2.com/products/enterprise-
service-bus/4.9.0/wso2esb-4.9.0.zip && \  
unzip /tmp/wso2esb-4.9.0.zip -d /opt && \  
rm -f /tmp/wso2esb-4.9.0.zip  
  
# Creates a default place to deploy carbonapps  
RUN ln -s /opt/wso2esb-4.9.0/repository/deployment/server/carbonapps
/carbonapps  
  
# Exporting ports  
EXPOSE 9443  
EXPOSE 9763  
EXPOSE 8243  
EXPOSE 8280  
# Configuring ESB  
COPY config/axis2.xml /opt/wso2esb-4.9.0/repository/conf/axis2/axis2.xml  
  
# Deploying jars  
COPY jars/lib/* /opt/wso2esb-4.9.0/repository/components/lib/  
  
# Patching  
COPY patches/ /opt/wso2esb-4.9.0/repository/components/patches/  
  
#Running ESB  
CMD ["/opt/wso2esb-4.9.0/bin/wso2server.sh"]  

