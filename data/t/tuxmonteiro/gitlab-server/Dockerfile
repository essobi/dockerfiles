FROM tuxmonteiro/centos6-dev  
  
MAINTAINER marcelotmonteiro@nospam.com  
  
WORKDIR /root  
  
USER root  
  
# gitlab requires redis >= 2.8 & mysql >= 5.5  
ENV PKG "mysql56u-server redis30u"  
RUN echo "Starting..."; \  
yum check-update -y; \  
yum install -y ${PKG}; \  
/etc/init.d/mysqld start; \  
/etc/init.d/redis start; \  
echo "Finished."  

