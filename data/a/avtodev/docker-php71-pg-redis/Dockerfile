FROM debian:jessie  
  
MAINTAINER "Avto Develop"  
LABEL Description="Basic docker image with PHP 7.1 (with some stuff) &
PostgreSQL & Redis" Vendor="avto-dev" Version="0.1"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV GNU_PARALLEL_VER 20180422  
RUN \  
apt-get -yq update && apt-get -yq upgrade -o Dpkg::Options::="--force-confold"
\  
&& apt-get -yq install --no-install-recommends apt-utils lsb-release apt-
transport-https curl sudo wget zip unzip \  
bzip2 git ssh ca-certificates make \  
&& wget http://ftp.gnu.org/gnu/parallel/parallel-${GNU_PARALLEL_VER}.tar.bz2
-O /tmp/parallel.tar.bz2 \  
&& mkdir /tmp/parallel/ \  
&& tar xvjf /tmp/parallel.tar.bz2 -C /tmp/parallel/ \  
&& cd /tmp/parallel/parallel-${GNU_PARALLEL_VER}/ && ./configure && make &&
make install \  
&& mkdir -p "$HOME/.ssh" && bash -c 'echo -e "\nHost
*\n\tStrictHostKeyChecking no\n\n" >> "$HOME/.ssh/config"'  
  
# php installation  
# ----------------  
RUN \  
curl -o /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get -yq update && apt-get install -y php7.1-common php7.1-cli
php7.1-xml php7.1-zip php7.1-curl php7.1-bcmath \  
php7.1-json php7.1-mbstring php7.1-pgsql php7.1-mcrypt php7.1-redis
php7.1-xdebug php7.1-sqlite3 php7.1-mysql \  
php7.1-gd \  
&& update-alternatives --set php $(which php7.1) \  
&& sed -i -r "s/display_errors = Off/display_errors = On/"
/etc/php/7.1/cli/php.ini \  
&& sed -i -r "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php/7.1/cli/php.ini \  
&& bash -c 'echo -e
"\n\nxdebug.profiler_enable=0\nxdebug.coverage_enable=1\nxdebug.remote_enable=0\n">>
/etc/php/7.1/mods-available/xdebug.ini'  
  
# composer installation  
# ---------------------  
ENV COMPOSER_HOME /usr/local/share/composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH "$COMPOSER_HOME:$COMPOSER_HOME/vendor/bin:$PATH"  
RUN \  
mkdir -pv $COMPOSER_HOME && chmod -R g+w $COMPOSER_HOME \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) \  
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); \  
echo 'Invalid installer' . PHP_EOL; exit(1); }" \  
&& php /tmp/composer-setup.php --filename=composer --install-
dir=$COMPOSER_HOME \  
&& $COMPOSER_HOME/composer --no-interaction global require 'hirak/prestissimo'
\  
&& $COMPOSER_HOME/composer --no-interaction global require 'deployer/deployer'
\  
&& $COMPOSER_HOME/composer --no-interaction global require 'avto-dev/php-cs-
fixer' '1.*' \  
&& $COMPOSER_HOME/composer global info  
  
# postgres installation  
# ---------------------  
RUN \  
wget https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add - \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg
main">> /etc/apt/sources.list.d/pgdg.list \  
&& apt-get -yq update && apt-get install -y postgresql-9.6 \  
&& mkdir /var/run/postgresql/9.6-main.pg_stat_tmp && chown -R
postgres:postgres /var/run/postgresql/9.6-main.pg_stat_tmp  
  
# redis installation  
# ------------------  
RUN \  
apt-get install -y redis-server \  
&& sed -i -r "s/daemonize yes/daemonize no/" /etc/redis/redis.conf  
  
# supervisor installation  
# -----------------------  
RUN \  
apt-get install -y supervisor  
ADD supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD supervisor/conf.d/ /etc/supervisor/conf.d/  
  
# make clean  
# ----------  
RUN apt-get -yqq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#VOLUME [ "/var/log/supervisor" ]  
# --> "Error: positional arguments are not supported"  
# http://stackoverflow.com/questions/22465003/error-positional-arguments-are-
not-supported  
#ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
EXPOSE 5666  

