FROM debian:wheezy  
RUN apt-get update -qq && apt-get upgrade -y  
RUN apt-get install wget -qq  
  
RUN apt-get update \  
&& apt-get install -y --force-yes \  
php5 \  
php5-fpm \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-curl \  
php5-gd \  
php5-intl  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
RUN php5enmod mcrypt  

