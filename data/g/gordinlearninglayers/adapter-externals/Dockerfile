FROM learninglayers/base  
MAINTAINER Andreas Guth <guth@dbis.rwth-aachen.de>  
  
# install dependencies for docker-gen  
# RUN apt-get -qqy --no-install-recommends install \  
# wget \  
# ca-certificates  
  
  
# add all files from conf subfolder to conf data volume  
# ADD conf/ /usr/local/openresty/conf/  
# ADD logs/ /usr/local/openresty/logs/  
  
  
# install docker gen, pull most recent nginx template file  
# ENV TEMPLDIR /usr/local/docker-gen/templates  
# RUN mkdir -p $TEMPLDIR \  
# && cd $TEMPLDIR \  
# && wget https://raw.githubusercontent.com/jwilder/docker-
gen/master/templates/nginx.tmpl \  
# && chmod 777 ngi*  
  
# provide volumes: openresty config, logs, docker-gen template path  
VOLUME ["/usr/local/openresty/conf/services/"]  
  
# take environment variable LAYERS_API_URI and replace in nginx config
template  
# CMD SERVER_NAME=`echo ${LAYERS_API_URI}| grep -oE '://[^/]+/' | cut -c4- |
rev | cut -c2- | rev` && \  
# sed -i "s/SERVER_NAME/${SERVER_NAME}/g" /usr/local/openresty/conf/nginx.conf  

