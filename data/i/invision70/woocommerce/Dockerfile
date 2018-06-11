FROM wordpress:php7.0-fpm  
MAINTAINER Kristian Østergaard Martensen <km@shipbeat.com>  
  
ENV WOOCOMMERCE_VERSION 2.6.4  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip wget \  
&& wget
https://downloads.wordpress.org/plugin/woocommerce.$WOOCOMMERCE_VERSION.zip -O
/tmp/temp.zip \  
&& cd /usr/src/wordpress/wp-content/plugins \  
&& unzip /tmp/temp.zip \  
&& rm /tmp/temp.zip \  
&& rm -rf /var/lib/apt/lists/*  
# Download WordPress CLI  
RUN curl -L "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar" > /usr/bin/wp && \  
chmod +x /usr/bin/wp  
  
VOLUME ["/var/www/html", "/usr/src/wordpress"]  

