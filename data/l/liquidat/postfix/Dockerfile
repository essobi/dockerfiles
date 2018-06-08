FROM centos:latest  
MAINTAINER liquidat, liquidat@bayz.de  
  
# install necessary packages  
RUN rpm --import https://getfedora.org/static/352C64E5.txt && rpm -Uvh
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum
-y update && yum -y install postfix cyrus-sasl cyrus-sasl-ldap cyrus-sasl-
plain pypolicyd-spf.noarch opendkim && yum clean all  
  
# copy docker entrypoint script  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# during container start, ensure proper directory rights and start Postfix  
ENTRYPOINT ["/bin/sh","-c","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 25 587 10025  

