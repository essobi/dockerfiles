################################################################################  
# Dockerfile for appserver.io example application  
################################################################################  
  
# base image  
FROM appserver/dist  
  
################################################################################  
  
# author  
MAINTAINER Tim Wagner <tw@appserver.io>  
  
################################################################################  
  
# add the sources to a temporary folder  
ADD . /tmp/example  
  
################################################################################  
  
# install composer dependencies  
RUN cd /tmp/example \  
&& composer install --prefer-dist --no-dev --no-interaction --optimize-
autoloader \  
&& mkdir /opt/appserver/webapps \  
&& mv /tmp/example/src /opt/appserver/webapps/example  
  
################################################################################  
  
# define default command  
ENTRYPOINT ["/usr/bin/supervisord"]

