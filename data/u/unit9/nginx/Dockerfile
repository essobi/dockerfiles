FROM unit9/base:latest  
  
MAINTAINER Krzysztof Skoracki <krzysztof.skoracki@unit9.com>  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends \  
nginx-light \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
EXPOSE 80  
COPY ["nginx.run", "/etc/service/nginx/run"]  
COPY ["rc.local", "/etc/rc.local"]  
COPY ["vhost.conf", "/etc/nginx/sites-available/default"]  

