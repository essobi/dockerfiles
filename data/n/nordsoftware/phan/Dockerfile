FROM php:7.1  
MAINTAINER Sam Stenvall <sam.stenvall@nordsoftware.com>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y git-core \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone --depth=1 https://github.com/nikic/php-ast.git \  
&& cd php-ast \  
&& phpize \  
&& ./configure \  
&& make install \  
&& echo 'extension=ast.so' > /usr/local/etc/php/php.ini \  
&& cd .. && rm -rf php-ast  
  
RUN curl --silent -L
https://github.com/etsy/phan/releases/download/0.9.2/phan.phar -o
/usr/local/bin/phan \  
&& chmod +x /usr/local/bin/phan  

