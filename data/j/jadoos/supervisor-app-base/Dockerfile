FROM jadoos/php-app-base:7  
MAINTAINER "Lukas Rosenstock" <lukas@jadoos-inc.com>  
  
# Install crontabs  
RUN yum -y install crontabs  
  
# Install supervisord  
RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python \  
&& easy_install supervisor  
  
# Set up starter script  
ADD start.sh /tmp/  
  
# Expose Gearman port  
EXPOSE 4730  
# Launch starter script  
CMD ["/bin/sh", "/tmp/start.sh"]  

