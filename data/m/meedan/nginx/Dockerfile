# meedan/nginx  
  
FROM ubuntu:16.04  
MAINTAINER sysops@meedan.com  
  
RUN useradd --no-create-home nginx -G www-data \  
&& apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
nginx-common \  
nginx-extras \  
ca-certificates  
  
CMD ["nginx","-g","daemon off;"]

