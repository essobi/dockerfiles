FROM ubuntu:16.04  
  
MAINTAINER Dylan <bbcheng@ikuai8.com>  
  
#############################################################################################  
# Locale, Language  
ENV OS_LOCALE="en_US.UTF-8"  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get install -y locales \  
&& locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LC_ALL=${OS_LOCALE} \  
LANGUAGE=en_US:en  
  
#############################################################################################  
# Allow ssh login  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y openssh-server tzdata \  
&& mkdir /var/run/sshd \  
&& ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
# RUN echo 'root:screencast' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
#############################################################################################  
# php env  
ENV PHP_RUN_DIR=/run/php \  
PHP_LOG_DIR=/var/log/php \  
PHP_CONF_DIR=/etc/php/5.6 \  
PHP_DATA_DIR=/var/lib/php  
  
#############################################################################################  
# php with extensions  
RUN DEBIAN_FRONTEND=noninteractive \  
buildDeps='software-properties-common python-software-properties' \  
# Install common libraries  
&& apt-get install --no-install-recommends -y $buildDeps \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
# Install PHP libraries  
&& apt-get install -y curl php5.6-fpm php5.6-cli php5.6-readline \  
php5.6-mbstring php5.6-zip php5.6-xml php5.6-json php5.6-bcmath php5.6-bz2 \  
php5.6-curl php5.6-mcrypt php5.6-gd php5.6-mysql php-pear \  
php-memcache php-memcached php-mongo php-mongodb php-redis \  
&& phpenmod mcrypt \  
# Cleaning  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./configs/php-fpm.conf ${PHP_CONF_DIR}/fpm/php-fpm.conf  
COPY ./configs/www.conf ${PHP_CONF_DIR}/fpm/pool.d/www.conf  
COPY ./configs/php.ini ${PHP_CONF_DIR}/fpm/conf.d/custom.ini  
  
RUN sed -i "s~PHP_RUN_DIR~${PHP_RUN_DIR}~g" ${PHP_CONF_DIR}/fpm/php-fpm.conf \  
&& sed -i "s~PHP_LOG_DIR~${PHP_LOG_DIR}~g" ${PHP_CONF_DIR}/fpm/php-fpm.conf \  
&& chown www-data:www-data ${PHP_DATA_DIR} -Rf  
  
WORKDIR /var/www  
  
EXPOSE 9000  
  
# PHP_DATA_DIR store sessions  
VOLUME ["${PHP_RUN_DIR}", "${PHP_DATA_DIR}"]  
CMD ["/usr/sbin/php-fpm5.6"]  

