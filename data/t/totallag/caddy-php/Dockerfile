FROM blitznote/debootstrap-amd64:16.10  
MAINTAINER Chris Phan <phanx068@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN addgroup --system caddy && adduser --system --ingroup caddy caddy  
WORKDIR /www  
  
ARG PHP_VERSION="7.1.3"  
ARG phplugins="+default"  
ARG plugins="http.git,http.realip,http.minify,http.filter"  
ARG buildDeps="libcurl4-openssl-dev build-essential autoconf automake
libxml2-dev libssl-dev libicu-dev libmcrypt-dev libbz2-dev libreadline-dev
libmhash-dev libicu-dev libxslt-dev"  
RUN apt-get update && \  
apt-get install -y aptitude && \  
aptitude install -y php7.0 php7.0-curl php7.0-json php7.0-cgi php7.0-fpm \  
openssl gettext libmcrypt4 libmhash2 $buildDeps && \  
curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew && \  
chmod +x phpbrew && \  
mv phpbrew /usr/local/bin/phpbrew && \  
phpbrew init && \  
echo "[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc" >> /root/.bashrc
&& \  
phpbrew install $PHP_VERSION $phplugins && \  
# clean up \  
phpbrew clean php-$PHP_VERSION && \  
apt-get purge -y --auto-remove aptitude $buildDeps && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
# allow environment variable access.  
RUN phpbrew switch php-$PHP_VERSION && \  
echo "clear_env = no" >> /root/.phpbrew/php/php-$PHP_VERSION/etc/php-fpm.conf  
  
# install caddy  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy && \  
chmod 0755 /usr/bin/caddy && \  
/usr/bin/caddy -version  
  
COPY Caddyfile /etc/Caddyfile  
  
EXPOSE 80 443 2015  
#USER caddy  
COPY index.php /www/index.php  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]

