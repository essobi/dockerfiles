# vim:set ft=dockerfile:  
# Base on VRT Base image  
FROM vrtsystems/baseimage:0.2.0  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# add our own user and group first to make sure their IDs get assigned  
# consistently, regardless of whatever dependencies get added later  
RUN groupadd -r nodejs && useradd -r -g nodejs nodejs  
  
ENV NODE_APP_PATH /opt/node_app  
  
RUN echo "=== Installing Node.js =================" \  
&& curl --silent --location https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs \  
&& mkdir /opt/node_app \  
&& echo "=== Cleaning up ========================" \  
&& /usr/local/sbin/docker-cleanup.sh  
  
COPY docker-entrypoint.sh /usr/local/sbin/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
  
CMD ["supervisor"]  

