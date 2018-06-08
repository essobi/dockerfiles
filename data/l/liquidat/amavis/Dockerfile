# amavis  
FROM centos:centos7  
MAINTAINER liquidat, liquidat@bayz.de  
  
# update yum and install postfix  
RUN rpm --import https://getfedora.org/static/352C64E5.txt && rpm -Uvh
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum
-y update && yum -y install amavisd-new spamassassin clamav-server clamav-
update && yum clean all  
  
# copy docker entrypoint  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# start postfix when container is started  
ENTRYPOINT ["/bin/sh","-c","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 10024  

