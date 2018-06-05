#  
# Uchiwa  
#  
# Pull base image.  
FROM ashangit/base:latest  
MAINTAINER Nicolas Fraison <nfraison@yahoo.fr>  
  
ENV UCHIWA_VERSION 0.13.0-1  
# Deploy Uchiwa  
RUN yum install
http://dl.bintray.com/palourde/uchiwa/uchiwa-${UCHIWA_VERSION}.x86_64.rpm -y  
  
# Mount sensu config.  
ADD conf/uchiwa.json /etc/sensu/uchiwa.json  
  
# Define working directory.  
WORKDIR /opt/uchiwa/src  
  
# Expose ports.  
EXPOSE 3000  
# Define default command.  
CMD /opt/uchiwa/bin/uchiwa -c /etc/sensu/uchiwa.json -p /opt/uchiwa/src/public  

