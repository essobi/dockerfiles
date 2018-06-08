FROM debian:stable as builder  
COPY rancherize.tgz /  
RUN mkdir /project  
WORKDIR /project  
RUN tar -xzf /rancherize.tgz  
  
FROM ipunktbs/php-composer:7.2.0-1.5.2  
ENV HOME=/home/user  
LABEL maintainer="Sven Speckmaier <sps@ipunkt.biz>"  
  
COPY \--from=builder /project /project  
ADD rancherize.tpl /opt/rancherize.tpl  
ADD rancherize.json /project/rancherize.json  
ADD entrypoint.sh /  
  
WORKDIR /project  
RUN chmod +x /entrypoint.sh \  
&& mkdir -p /home/user \  
&& apt-get update \  
&& apt-get -y install libssh2-1-dev \  
&& rm -Rf /var/lib/apt/lists/* \  
&& pecl install -a ssh2-1.0 \  
&& docker-php-ext-enable ssh2 \  
&& vendor/bin/rancherize plugin:register ipunkt/rancherize-backup-storagebox \  
&& vendor/bin/rancherize plugin:register ipunkt/rancherize-publish-traefik-
rancher  
  
ENTRYPOINT ["bash", "/entrypoint.sh"]  

