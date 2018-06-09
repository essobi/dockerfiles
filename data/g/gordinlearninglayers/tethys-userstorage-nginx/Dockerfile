FROM learninglayers/base  
  
MAINTAINER Andreag Guth  
  
# add nginx config  
ADD nginx /usr/local/openresty/conf/services/tethys/  
  
# provide config as volume  
VOLUME ["/usr/local/openresty/conf/services/tethys/"]  

