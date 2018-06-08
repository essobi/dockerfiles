FROM wordpress:latest  
MAINTAINER supermomonga  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sendmail \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip mbstring  

