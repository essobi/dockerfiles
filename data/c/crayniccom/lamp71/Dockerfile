FROM ubuntu:16.04  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y language-pack-en-base &&
\  
locale-gen en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
add-apt-repository ppa:ondrej/php  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
php7.1 \  
php7.1-curl \  
php7.1-cli \  
php7.1-gd \  
php7.1-bcmath \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-xml \  
php7.1-xsl \  
php7.1-zip \  
libapache2-mod-php7.1  
  
  
COPY config /  
  
WORKDIR /var/www/html  
EXPOSE 80 443  
  
CMD bash -C "/entrypoint.sh"  

