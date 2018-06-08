FROM mcuyar/docker-alpine-nginx-php7:debug  
MAINTAINER Matthew Cuyar <matt@enctypeapparel.com>  
##/  
# Install Lumen CLI  
#/  
RUN cd /var \  
&& rm -rf www \  
&& composer create-project \--prefer-dist laravel/lumen www \  
&& composer clearcache  
  
##/  
# Copy files  
#/  
COPY rootfs /

