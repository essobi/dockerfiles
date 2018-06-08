# Custom PHP drush container  
FROM nascom/php:5.6-composer  
  
MAINTAINER Wim Vandersmissen <wim.vandersmissen@nascom.be>  
  
# Install Mysql client tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install drush  
RUN composer global require drush/drush:8.* --prefer-dist  
  
ENTRYPOINT ["drush"]  

