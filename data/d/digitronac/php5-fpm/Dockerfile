FROM debian:jessie  
MAINTAINER Nemanja Ognjanovic <nemanja.ognjanovic@ringieraxelspringer.rs>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
RUN sed --in-place 's/httpredir.debian.org/mirror.sov.uk.goscomb.net/'
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y --no-install-recommends install locales apt-utils  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
RUN /usr/sbin/update-locale LANG=en_US.UTF-8  
RUN apt-get -y --no-install-recommends install ca-certificates \  
build-essential \  
git \  
vim \  
php5-dev \  
php5-fpm \  
php5-apcu \  
php5-intl \  
php5-mysql \  
mysql-client \  
php5-igbinary \  
php5-memcache \  
php5-xdebug \  
php5-redis \  
php5-cli \  
php5-sqlite \  
php5-mcrypt \  
php5-curl \  
php-gettext \  
php5-gd \  
php5-imagick \  
imagemagick \  
openssh-client \  
wget \  
curl \  
software-properties-common \  
gettext \  
zip \  
apt-transport-https  
  
# phalcon  
RUN git clone -q --depth=1 https://github.com/phalcon/cphalcon.git -b 1.3.3  
WORKDIR /cphalcon/ext  
RUN export CFLAGS="-g3 -O1 -fno-delete-null-pointer-checks -Wall";  
RUN phpize  
RUN ./configure --enable-phalcon  
RUN make -j4  
RUN make install  
WORKDIR /  
RUN rm -rf /cphalcon  
RUN touch /etc/php5/cli/conf.d/50-phalcon.ini  
RUN echo "extension=phalcon.so" > /etc/php5/cli/conf.d/50-phalcon.ini  
RUN touch /etc/php5/fpm/conf.d/50-phalcon.ini  
RUN echo "extension=phalcon.so" > /etc/php5/fpm/conf.d/50-phalcon.ini  
  
RUN apt-get autoclean && apt-get clean && apt-get autoremove  
  
# fpm listens on 9000  
RUN sed -i 's/listen = \/var\/run\/php5-fpm.sock/listen = 9000/g'
/etc/php5/fpm/pool.d/www.conf  
# do not run as deamon so that it could run as executable  
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf  
# var order  
RUN sed -ri -e "s/^variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/cli/php.ini  
  
RUN rm -rf /root/.composer /tmp/* /var/lib/apt/lists/*  
  
EXPOSE 9000  
#CMD ["/usr/sbin/php5-fpm"]  

