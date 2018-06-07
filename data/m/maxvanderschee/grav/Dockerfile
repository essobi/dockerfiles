FROM maxvanderschee/nginx-php  
  
LABEL maintainer "m.v.d.schee@ewake.nl"  
  
# Install core packages for Grav.  
RUN apt-get update -q  
RUN apt-get install -y php7.0-cli php7.0-gd php7.0-curl php7.0-mbstring
php7.0-xml php7.0-zip php-apcu  
RUN apt-get clean -q && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup nginx config  
WORKDIR /etc/nginx/snippets/  
COPY security.conf security.conf  
  
# Set execute work directory  
WORKDIR /var/www/app  

