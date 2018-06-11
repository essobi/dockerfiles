# docker run -dt -p 80:8080 -v /home/upsource:/data/upsource --restart=always
--name=upsource-2.5 pluribuslabs/centos7-jetbrains-upsource:2.5  
FROM pluribuslabs/centos7-oracle-jdks-7-8  
MAINTAINER Pluribus Labs Docker Dev <docker-dev@pluribuslabs.com>  
ENV HUB_PACKAGE_BASE_NAME upsource-3.0.4346  
ENV HUB_PACKAGE $HUB_PACKAGE_BASE_NAME.zip  
ENV HUB_DOWNLOAD https://download.jetbrains.com/upsource  
ENV HUB_DATA_PATH /data/upsource  
ENV HUB_CONF_PATH /opt/Upsource/conf  
  
#set limits for upsource per documentation  
RUN yum -y install wget hostname unzip net-tools && \  
echo '* - memlock unlimited' >> /etc/security/limits.conf && \  
echo '* - nofile 100000' >> /etc/security/limits.conf && \  
echo '* - nproc 32768' >> /etc/security/limits.conf && \  
echo '* - as unlimited' >> /etc/security/limits.conf && \  
wget -nv $HUB_DOWNLOAD/$HUB_PACKAGE && \  
unzip $HUB_PACKAGE -d /opt && \  
mv /opt/$HUB_PACKAGE_BASE_NAME /opt/Upsource && \  
rm $HUB_PACKAGE  
  
EXPOSE 8080  
VOLUME ["/data/upsource"]  
VOLUME ["/opt/Upsource/conf"]  
  
# Looks like ENV variables don't get subbed in the CMD command hence the
hardcode of values  
# from
https://confluence.jetbrains.com/display/YTD6/YouTrack+JAR+as+a+Service+on+Linux  
CMD ["/opt/Upsource/bin/upsource.sh", "run"]  

