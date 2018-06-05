FROM conchoid/docker-phpenv:v1-8-5.6-alpine3.6  
ENV PHP_CONFIGURE_OPTS "--disable-fpm --disable-cgi"  
ENV PREINSTALLED_VERSIONS "\  
5.3.29\n\  
5.4.45\n\  
5.5.38\n\  
5.6.34\n\  
7.0.28\n\  
7.1.15\n\  
7.2.3"  
RUN set -x \  
&& phpenv global system \  
&& system_php_ver="5.6.34" \  
&& version_bin_dir="${PHPENV_ROOT}/versions/${system_php_ver}/bin" \  
&& mkdir -p "${version_bin_dir}" \  
&& cp "$(phpenv which php)" "${version_bin_dir}" \  
&& cp "$(phpenv which php-config)" "${version_bin_dir}" \  
&& cp "$(phpenv which phar)" "${version_bin_dir}" \  
&& cp "$(phpenv which phar.phar)" "${version_bin_dir}" \  
&& export CONFIGURE_OPTS="${PHP_CONFIGURE_OPTS}" \  
&& export CFLAGS="${PHP_CFLAGS}" \  
&& echo -e "${PREINSTALLED_VERSIONS}" | while read version;do \  
if [ ! -e "${PHPENV_ROOT}/versions/${version}" ];then \  
phpenv install $version \  
&& phpenv global $version \  
# Add the timezone settings to php.ini to avoid date function wargnings.  
&& php --ini | grep 'Loaded Configuration File' | awk -F':' '{ print $2 }' |
xargs -i /bin/sh -c 'echo -e "[Date]\ndate.timezone = UTC" >> {}';fi;done \  
&& rm -rf "/tmp/php-build*" \  
&& phpenv global system  

