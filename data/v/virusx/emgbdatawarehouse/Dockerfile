FROM java:8-jre-alpine  
RUN apk add \--update wget bash && \  
cd /usr/local/share/ && \  
wget \--progress=dot:giga "https://openstack.cebitec.uni-
bielefeld.de:8080/swift/v1/virusx_public/EMGBDataWarehouse-0.4.2.jar" && \  
apk del wget bash && \  
rm -rf /var/cache/apk/*  

