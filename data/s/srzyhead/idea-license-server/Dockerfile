FROM ubuntu:14.04  
MAINTAINER srzyhead<srzyhead@yeah.net>  
  
WORKDIR /root  
  
ADD ./IntelliJIDEALicenseServer_linux_amd64
/root/IntelliJIDEALicenseServer_linux_amd64  
  
RUN chmod 777 ./IntelliJIDEALicenseServer_linux_amd64  
  
EXPOSE 41017  
#run license server  
CMD ./IntelliJIDEALicenseServer_linux_amd64

