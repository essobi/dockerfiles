#  
# Lapis Web Framework  
#  
FROM gmesalazar/openresty  
  
MAINTAINER Guilherme Salazar <gmesalazar@gmail.com>  
  
RUN \  
apk add --no-cache --virtual .build \  
unzip \  
build-base \  
openssl-dev && \  
luarocks install lapis && \  
apk del .build  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["sh", "docker-entrypoint.sh"]  

