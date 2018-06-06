FROM ubuntu:trusty  
MAINTAINER Chris Hardekopf <chrish@basis.com>  
  
# Install websvn  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y websvn \  
apache2-utils && \  
rm -rf /var/lib/apt/lists/*  
  
# Replace the http URL in wsvn.php  
RUN perl -pi -e \  
"s/^\\\\\$locwebsvnhttp =.+;\$/\\\\\$locwebsvnhttp = '';/g" \  
/etc/websvn/wsvn.php  
  
# Use parent path for svn archives  
RUN perl -pi -e \  
"s/\/\/
\\\\\$config->parentPath([^,]+);\$/\\\\\$config->parentPath('\/svn');/g" \  
/etc/websvn/config.php  
# Enable MultiViews  
RUN perl -pi -e \  
"s/\/\/
\\\\\$config->useMultiViews([^,]+);\$/\\\\\$config->useMultiViews();/g" \  
/etc/websvn/config.php  
# Set up auth  
RUN perl -pi -e \  
"s/\/\/
\\\\\$config->useAuthenticationFile([^,]+);/\\\\\$config->useAuthenticationFile('\/svn\/svn.authz');/g"
\  
/etc/websvn/config.php  
  
# Add the websv apache configuration and enable the site  
ADD websvn.conf /etc/apache2/sites-available/  
RUN a2enmod expires auth_digest authz_groupfile && \  
a2dissite 000-default && a2ensite websvn  
  
# Add the start script  
ADD start /opt/  
  
# Archives and configuration are stored in /svn  
VOLUME [ "/svn" ]  
  
# Expose public port for web server  
EXPOSE 80  
# Initialize configuration and run the web server  
CMD [ "/opt/start" ]  
  

