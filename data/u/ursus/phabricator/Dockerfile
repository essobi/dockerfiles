FROM ursus/nginx-php5-fpm:latest  
MAINTAINER Djordje Stojanovic <djordje.stojanovic@ursus.rs>  
LABEL vendor="Ursus Software"  
  
RUN apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qq -y php5-gd php5-curl
php-apc php5-mysql php5-json python-pygments sendmail \  
&& apt-get clean -qq  
  
RUN mkdir -p /opt && cd /opt \  
&& git clone https://github.com/phacility/libphutil.git \  
&& git clone https://github.com/phacility/arcanist.git \  
&& git clone https://github.com/phacility/phabricator.git  
RUN mkdir -p /var/phabricator/{repo,uploads}  
  
COPY nginx/phabricator.conf /etc/nginx/sites-available/default  
COPY supervisor/conf.d/phabricator.conf
/etc/supervisor/conf.d/phabricator.conf  
  
COPY phd-run.sh /usr/bin/phd-run  
RUN chmod 775 /usr/bin/phd-run  
  
VOLUME /var/phabricator/repo /var/phabricator/uploads  
  
# CMD ["/usr/bin/supervisord", "-c",
"/etc/supervisor/conf.d/phabricator.conf"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

