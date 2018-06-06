FROM debian:jessie  
ARG DOMAINE="zamaroczy.fr"  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM=xterm \  
DIRPATH="/usr/bin" \  
CWD_NGINX="/etc/nginx" \  
RC_VERSION="1.3.4" \  
DOMAINE=${DOMAINE}  
MAINTAINER Jerome Zamaroczy  
  
LABEL vendor=ACME\ Incorporated \  
$DOMAINE.roundcube-beta="roundcubemail-$RC_VERSION-complete" \  
$DOMAINE.roundcube-production="prod" \  
$DOMAINE.version="$RC_VERSION-complete" \  
$DOMAINE.release-date="2017-03-31"  
  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y --no-install-recommends \  
nginx php5-fpm nano wget sqlite3 procps \  
php5-mcrypt php5-intl php5-sqlite php-pear \  
php-net-smtp php-mail-mime  
  
WORKDIR /usr/share/nginx/  
  
RUN \  
wget --no-check-certificate
https://github.com/roundcube/roundcubemail/releases/download/$RC_VERSION/roundcubemail-$RC_VERSION-
complete.tar.gz -O - | tar xz ;\  
rm -fr /usr/share/nginx/www ;\  
mv roundcubemail-$RC_VERSION /usr/share/nginx/www ;  
  
ADD config.inc.php /usr/share/nginx/www/config/  
ADD nginx.conf $CWD_NGINX/nginx.conf  
ADD default $CWD_NGINX/sites-enabled/default  
ADD docker-entrypoint.sh $DIRPATH/  
  
WORKDIR $DIRPATH  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
RUN chmod +x docker-entrypoint.sh  
EXPOSE 80  
CMD [ "bash", "docker-entrypoint.sh" ]  
  

