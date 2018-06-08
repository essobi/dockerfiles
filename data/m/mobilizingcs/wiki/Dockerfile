FROM nginx  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y curl git php5-fpm \  
&& curl -fSL http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz -o
/tmp/dokuwiki-stable.tgz \  
&& mkdir /var/www \  
&& tar xvf /tmp/dokuwiki-stable.tgz -C /var/www --strip-components=1 \  
&& git clone \--single-branch https://github.com/mobilizingcs/wiki
/var/www/data/git \  
&& git clone \--single-branch https://github.com/arsava/dokuwiki-template-
vector /var/www/lib/tpl/vector \  
&& apt-get purge -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
ADD php-pool-www.conf /etc/php5/fpm/pool.d/www.conf  
ADD dokuwiki-local.php /var/www/conf/local.php  
  
# copies mobilize logo to vector template  
RUN cp /var/www/data/git/media/wiki/logo.png /var/www/lib/tpl/vector/user/  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
RUN chown -R nginx.nginx /var/www  
  
CMD ["/run.sh"]

