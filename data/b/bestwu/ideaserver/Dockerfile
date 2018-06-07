FROM busybox:latest  
MAINTAINER Peter Wu <piterwu@outlook.com>  
ENV u Peter  
EXPOSE 1017  
COPY IntelliJIDEALicenseServer_linux_amd64
/IntelliJIDEALicenseServer_linux_amd64  
RUN chmod +x /IntelliJIDEALicenseServer_linux_amd64  
CMD /IntelliJIDEALicenseServer_linux_amd64 -u=$u

