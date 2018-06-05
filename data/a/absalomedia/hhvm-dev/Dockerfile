FROM absalomedia/nginx-pagespeed  
  
MAINTAINER Lawrence Meckan <media@absalom.biz>  
  
RUN apt-get update && \  
apt-get install -y hhvm hhvm-dev autoconf automake binutils-dev build-
essential cmake g++ gawk git \  
libboost-dev libboost-filesystem-dev libboost-program-options-dev libboost-
regex-dev \  
libboost-system-dev libboost-thread-dev libboost-context-dev libbz2-dev libc-
client-dev libldap2-dev \  
libc-client2007e-dev libcap-dev libdouble-conversion-dev libcurl4-openssl-dev
libdwarf-dev libelf-dev \  
libexpat-dev libgd2-xpm-dev libgoogle-glog-dev libgoogle-perftools-dev libicu-
dev \  
libjemalloc-dev libmcrypt-dev libmemcached-dev libmysqlclient-dev libncurses-
dev \  
libonig-dev libpcre3-dev libreadline-dev libtbb-dev libtool libxml2-dev
zlib1g-dev \  
libevent-dev libmagickwand-dev libinotifytools0-dev libiconv-hook-dev libedit-
dev \  
libiberty-dev libxslt1-dev ocaml-native-compilers libsqlite3-dev libyaml-dev
libgmp3-dev \  
gperf libkrb5-dev libnotify-dev && \  
apt-get clean  
  
RUN mkdir /root/bin/ && \  
echo "export PATH=/root/bin:$PATH" > /root/.bashrc  
  
EXPOSE 443  
EXPOSE 80  
  
ENV DEFAULT_APP_ENV production  
ENV DEFAULT_CHOWN_APP_DIR true  
ENV DEFAULT_VIRTUAL_HOST example.com  
ENV DEFAULT_TIMEZONE Australia/Brisbane  
ENV DEFAULT_APP_USER nginx-php  
ENV DEFAULT_APP_GROUP nginx-php  
ENV DEFAULT_APP_UID 1000  
ENV DEFAULT_APP_GID 1000  
ENV DEFAULT_UPLOAD_MAX_SIZE 30M  
ENV DEFAULT_NGINX_MAX_WORKER_PROCESSES 8  
ENV DEFAULT_NGINX_KEEPALIVE_TIMEOUT 30  
ENV DEFAULT_PHP_MEMORY_LIMIT 128M  
ENV DEFAULT_PHP_PROCESS_MANAGER dynamic  
ENV DEFAULT_PHP_MAX_CHILDREN 6  
ENV DEFAULT_PHP_START_SERVERS 3  
ENV DEFAULT_PHP_MIN_SPARE_SERVERS 2  
ENV DEFAULT_PHP_MAX_SPARE_SERVERS 3  
ENV DEFAULT_PHP_MAX_REQUESTS 500  
  
COPY . /app  
  
RUN chmod 750 /app/bin/*  
  
RUN /app/bin/init_hhvm.sh  
  
ENTRYPOINT ["/app/bin/boot.sh"]  
  
CMD ["/sbin/my_init"]

