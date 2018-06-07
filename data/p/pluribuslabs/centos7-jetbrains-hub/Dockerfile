# docker run -dt -p 8110:8110 pluribuslabs/centos7-jetbrains-hub  
FROM pluribuslabs/centos7-oracle-jdks-7-8  
MAINTAINER Pluribus Labs Docker Dev <docker-dev@pluribuslabs.com>  
  
ENV APP_VERSION 2.0  
ENV APP_REVISION 85  
ENV APP_BUILD $APP_VERSION.$APP_REVISION  
  
ENV HUB_PACKAGE hub-ring-bundle-$APP_BUILD  
ENV HUB_DOWNLOAD https://download.jetbrains.com/hub/$APP_VERSION  
  
ENV HUB_DATA_PATH /data/jetbrains_hub  
  
RUN yum -y install wget unzip net-tools && \  
wget -nv --output-document=hub.zip $HUB_DOWNLOAD/$HUB_PACKAGE.zip && \  
unzip hub.zip -d /opt && \  
rm hub.zip && \  
mkdir -p $HUB_DATA_PATH/data && \  
mkdir -p $HUB_DATA_PATH/backups && \  
mkdir -p $HUB_DATA_PATH/logs && \  
mkdir -p $HUB_DATA_PATH/temp && \  
mv /opt/$HUB_PACKAGE /opt/hub  
  
EXPOSE 8110 8080  
VOLUME ["/data/jetbrains_hub"]  
VOLUME ["/opt/hub/conf"]  
VOLUME ["/opt/hub/data"]  
  
# Looks like ENV variables don't get subbed in the CMD command hence the
hardcode of values  
# from
https://confluence.jetbrains.com/display/YTD6/YouTrack+JAR+as+a+Service+on+Linux  
CMD ["/opt/hub/bin/hub.sh", "run", "--listen-port=8110"]  

