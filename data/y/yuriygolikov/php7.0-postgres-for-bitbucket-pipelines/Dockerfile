FROM ubuntu:14.04  
ENV INITRD=No TERM=dumb MY_TZ=America/New_York  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /etc/timezone && echo $MY_TZ >> /etc/timezone && locale-gen en_US.UTF-8
&& LC_ALL=en_US.UTF-8  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Install LAMP stack  
RUN apt-get update  
RUN apt-get install -y python-software-properties software-properties-common
&& apt-get update && apt-get -qq upgrade  
RUN LC_ALL=fr_FR.UTF-8 add-apt-repository ppa:ondrej/mysql-5.6 -y && apt-get
update  
RUN apt-add-repository ppa:ondrej/php  
# Install needed packages here  
RUN apt-get update && apt-get install -y --force-yes \  
git \  
vim \  
php7.0 \  
php7.0-cli \  
php7.0-dev \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-pgsql \  
php7.0-mcrypt \  
php7.0-gd \  
php-imagick \  
php7.0-curl \  
php7.0-intl \  
php7.0-common \  
php7.0-json \  
php7.0-opcache \  
php7.0-recode \  
php7.0-soap \  
php7.0-xml \  
php7.0-zip \  
php7.0-opcache \  
php-apcu \  
php-gettext \  
postgresql-9.3 \  
postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
redis-server  
  
RUN curl -sSL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -y --no-install-recommends install nodejs  
  
RUN curl https://getcomposer.org/installer | php -- && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
RUN apt-get autoclean && apt-get autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER postgres  
  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER root WITH SUPERUSER PASSWORD 'root';" &&\  
createdb -O root test  
  
RUN echo "host all all localhost md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

