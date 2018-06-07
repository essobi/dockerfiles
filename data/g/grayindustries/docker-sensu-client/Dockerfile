FROM grayindustries/docker-sensu-base  
MAINTAINER Greg Poirier <grep@gray.industries>  
  
ADD files/settings.json /etc/sensu/settings.json  
ADD files/sensu-client.sh /sensu-client.sh  
ADD files/supervisord-sensu-client.conf /etc/supervisor/conf.d/sensu-
client.conf  

