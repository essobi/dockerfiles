FROM centos  
  
# Frist of all update the system then install the epel repository after that
install basic packages like python-setuptools, is required to have python's
easy_install, yum-utils so we have yum-config-manager tool available, inotify
is needed to automate daemon restarts after config file changes and jq, small
library for handling JSON files/api from CLI and finally clean the Cache.  
RUN \  
yum update -y && \  
yum install -y epel-release && \  
yum install -y iproute python-setuptools hostname inotify-tools yum-utils
which jq && \  
yum clean all  
  
# Install supervisord (via python's easy_install)  
RUN easy_install supervisor  
  
# Update the system and then install some basic web-related tools.  
RUN \  
yum update -y && \  
yum install -y wget patch tar bzip2 unzip  
  
#Add give all permission to /var/ftp/pub dirctory for ftp anonymous user, to
upload or download files.  
RUN \  
mkdir -p /var/ftp/pub && \  
chmod -R 777 /var/ftp/pub  
# Install apache server  
RUN \  
yum install -y httpd  
  
# Install ftp server  
RUN \  
yum install -y vsftpd  
  
# Clean YUM caches to minimise Docker image size...  
RUN \  
yum clean all && rm -rf /tmp/yum*  
  
ENV USER=www  
ENV PASSWORD=iaw  
  
# Add supervisord conf, bootstrap.sh files  
ADD container-files /  
  
# Add index.html to /var/www/html/ this is the page, that will display on your
browser once you enter your Apeche Server.  
ADD index.html /var/www/html/  
  
#Add prova file to /var/ftp/pub  
ADD prova /var/ftp/pub  
  
# Add vsftpd.conf file to /etc/vsftpd  
ADD vsftpd.conf /etc/vsftpd/  
  
#Run the sed command to assign USER and PASSWORD environment variable to
/etc/supervisord.conf and /config/init/supervisor_setcre.sh files.  
RUN \  
sed -ri "s/www/${USER}/g" /etc/supervisord.conf && \  
sed -ri "s/iaw/${PASSWORD}/g" /etc/supervisord.conf && \  
sed -ri "s/www/${USER}/g" /config/init/supervisor_setcre.sh && \  
sed -ri "s/iaw/${PASSWORD}/g" /config/init/supervisor_setcre.sh  
  
#Create volume /var/www/html for Apache Server and /var/ftp/pub for FTP
server.  
VOLUME ["/var/www/html, /var/ftp/pub"]  
  
#Expose the port 80 for apache, 21 and 20 for ftp and 9001 for supervisord.  
EXPOSE 80 20 21 9001  
#It iterates through all /config/init/*.sh scripts and runs them, then
launches supervisord.  
ENTRYPOINT ["/config/bootstrap.sh"]  

