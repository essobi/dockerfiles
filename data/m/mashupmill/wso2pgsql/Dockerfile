FROM postgres:9.3  
  
ENV POSTGRES_DB=wso2carbon_db \  
POSTGRES_USER=wso2 \  
POSTGRES_PASSWORD=wso2  
  
# Add init scripts  
ADD init-wso2.sh /docker-entrypoint-initdb.d/init-wso2.sh  
  
# This is the pre-packaged identity server 5.0.0 with api manager 1.9.1  
# Came from https://docs.wso2.com/display/CLUSTER420/Configuring+the+Pre-
Packaged+Identity+Server+5.0.0+with+API+Manager+1.9.1  
  
RUN apt-get update && apt-get install -y unzip wget && \  
wget -P /opt/ http://product-dist.wso2.com/downloads/api-
manager/1.9.1/identity-server/wso2is-5.0.0.zip && \  
unzip /opt/wso2is-5.0.0.zip wso2is-5.0.0/dbscripts/* -d /opt && \  
mv /opt/wso2is-5.0.0 /opt/wso2 && \  
rm /opt/wso2is-5.0.0.zip && \  
chmod a+x /docker-entrypoint-initdb.d/*.sh  
  
# Clean up/slim  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

