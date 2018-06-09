FROM cheggwpt/php5-nginx:0.0.1  
# Tideways ENVs  
ENV TIDEWAYS_PORT_UDP 8135  
ENV TIDEWAYS_PORT_TCP 9135  
ENV TIDEWAYS_ENV production  
ENV tideways_version 1.5.3  
ENV tideways_ext_version 4.0.7  
ENV tideways_php_version 2.0.14  
ENV tideways_dl https://github.com/tideways/  
ENV php_ini_dir /etc/php5/conf.d  
  
# Load ash profile on launch  
ENV ENV=/etc/profile  
  
RUN apk --update add --virtual .build_package \  
git curl file build-base autoconf  
  
RUN apk add --virtual .build_libraries \  
libpcre16 \  
libpcre32 \  
libpcrecpp \  
pcre-dev \  
php5-dev  
  
# Build & install ext/tideways & Tideways.php (props to till)  
RUN cd /tmp && \  
curl -L "${tideways_dl}/php-profiler-
extension/archive/v${tideways_ext_version}.zip" \  
\--output "/tmp/v${tideways_ext_version}.zip" && \  
cd /tmp && unzip "v${tideways_ext_version}.zip" && \  
cd "php-xhprof-extension-${tideways_ext_version}" && \  
phpize && \  
./configure && \  
make && make install && \  
echo 'extension=tideways.so' > "${php_ini_dir}/22_tideways.ini" && \  
curl -L
"${tideways_dl}/profiler/releases/download/v${tideways_php_version}/Tideways.php"
\  
\--output "$(php-config --extension-dir)/Tideways.php" && \  
ls -l "$(php-config --extension-dir)/Tideways.php" && \  
cd /tmp && rm -rf php-xhprof-extension-${tideways_ext_version}/
v${tideways_ext_version}.zip  
  
# install the tideways daemon  
RUN cd /tmp && \  
wget https://s3-eu-
west-1.amazonaws.com/tideways/daemon/${tideways_version}/tideways-
daemon-v${tideways_version}-alpine.tar.gz && \  
tar -zxf tideways-daemon-v${tideways_version}-alpine.tar.gz && \  
mv build/dist/tideways-daemon /usr/bin && \  
ls -l /usr/bin/tideways-daemon && \  
mkdir -p /var/run/tideways && \  
cd /tmp && rm -rf build/ tideways-daemon-v${tideways_version}-alpine.tar.gz  
  
RUN apk del .build_package .build_libraries && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
# dump some build done info on PHP  
RUN php -m && php --ini  
  
# Add the config  
COPY container_confs /  
  
#  
RUN chmod a+rwx /start_tideways.sh  

