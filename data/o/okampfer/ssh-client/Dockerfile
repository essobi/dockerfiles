FROM gliderlabs/alpine:3.5  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
RUN apk-install openssh-client  
  
# Security fix for CVE-2016-0777 and CVE-2016-0778  
RUN echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config  
  
ENTRYPOINT ["ssh"]  

