FROM centos  
MAINTAINER stars_kim<stars_kim@163.com>  
ADD . /IDEA  
RUN yum -y update && \  
yum -y upgrade && \  
yum clean all && \  
chmod -R 755 /IDEA  
WORKDIR /IDEA  
EXPOSE 1027  
CMD ./IntelliJIDEALicenseServer_linux_amd64 -u Stars_Kim  

