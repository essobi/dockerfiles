FROM berlingskemedia/bm.docker.php:testing-latest  
MAINTAINER Casper Bruun <cbm@berlingskemedia.dk>  
  
ENV REFRESHED_AT="2017-10-16 15:30:00"  
  
# Install NewRelic agent  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' >
/etc/apt/sources.list.d/newrelic.list \  
&& curl -s https://download.newrelic.com/548C16BF.gpg | apt-key add \- \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
newrelic-php5 \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -f /etc/php/7.2/{fpm,cli}/conf.d/newrelic.ini  
  
# Install BlackFire.io probe  
# https://blackfire.io/docs/integrations/docker  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& rm -f /tmp/blackfire-probe.tar.gz \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php/7.2/mods-available/blackfire.ini \  
&& ln -s /etc/php/7.2/mods-available/blackfire.ini
/etc/php/7.2/fpm/conf.d/20-blackfire.ini \  
&& ln -s /etc/php/7.2/mods-available/blackfire.ini
/etc/php/7.2/cli/conf.d/20-blackfire.ini  
  
# Overwrite existing runit.sh script with NewRelic enabled version  
ADD runit.sh /  

