FROM learninglayers/base  
MAINTAINER Yordan Manolov <manolov@dbis.rwth-aachen.de>  
  
# add all files from conf subfolder to conf data volume  
ADD conf/ /usr/local/openresty/conf/  
#ADD logs/ /usr/local/openresty/logs/  
ENV ORDIR /usr/local/openresty  
# here goes nginx.conf  
VOLUME ["$ORDIR/conf"]  
## here go the .conf files of all backend services  
#VOLUME ["$ORDIR/conf/services"]  
# take environment variable LAYERS_API_URI and replace in nginx config
template  
CMD SERVER_NAME=`echo ${LAYERS_API_URI}| grep -oE '://[^/]+/' | cut -c4- | rev
| cut -c2- | rev` && \  
sed -i "s/SERVER_NAME/${SERVER_NAME}/g" /usr/local/openresty/conf/nginx.conf  
  

