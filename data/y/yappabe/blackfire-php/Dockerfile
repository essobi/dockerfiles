FROM yappabe/php:7.1  
ENV BLACKFIRE_LOG_LEVEL 1  
ENV BLACKFIRE_LOG_FILE /tmpfs/logs/blackfire.log  
ENV BLACKFIRE_SOCKET unix:///var/run/blackfire/agent.sock  
  
RUN wget -O - https://packagecloud.io/gpg.key | apt-key add - && \  
echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
RUN \  
apt-get update && \  
apt-get install -y \  
blackfire-agent \  
blackfire-php  
  
RUN curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/71 \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so  
  
COPY blackfire-agent.ini /etc/blackfire/agent  
COPY blackfire-php.ini /etc/php/7.1/fpm/conf.d/92-blackfire-config.ini  
COPY blackfire-php.ini /etc/php/7.1/cli/conf.d/92-blackfire-config.ini  
  
COPY blackfire-run.sh /blackfire-run.sh  
  
ENTRYPOINT ["/bin/bash", "/blackfire-run.sh"]  

