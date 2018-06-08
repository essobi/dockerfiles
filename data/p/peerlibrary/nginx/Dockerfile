FROM peerlibrary/runit  
  
MAINTAINER Mitar <mitar.docker@tnode.com>  
  
EXPOSE 80/tcp  
  
RUN apt-get update -q -q && \  
apt-get install nginx-full --yes --force-yes && \  
echo 'daemon off;' >> /etc/nginx/nginx.conf && \  
sed -i 's/\/\$nginx_version//' /etc/nginx/fastcgi_params  
  
COPY ./etc /etc  

