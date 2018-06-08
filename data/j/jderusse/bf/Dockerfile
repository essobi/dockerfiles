FROM alpine:3.6  
  
RUN apk add --no-cache \  
php7 \  
php7-session \  
curl  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& rm /tmp/blackfire-probe.tar.gz \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php7/conf.d/blackfire.ini \  
  
&& curl -A "Docker" -o /usr/local/bin/blackfire -D - -L -s
https://packages.blackfire.io/binaries/blackfire-agent/1.12.0/blackfire-cli-
linux_static_amd64 \  
&& chmod +x /usr/local/bin/blackfire \  
  
&& php --ri blackfire  

