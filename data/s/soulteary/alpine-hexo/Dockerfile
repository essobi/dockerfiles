FROM soulteary/alpine-node:6.7.0  
MAINTAINER soulteary <soulteary@gmail.com>  
  
RUN mkdir -p /data/website && \  
mkdir -p /data/docker && \  
mkdir -p /data/website/logs  
  
WORKDIR /data/website  
  
RUN npm install hexo-cli -g --registry=https://registry.npm.taobao.org \  
&& hexo init . \  
&& npm install --production --registry=https://registry.npm.taobao.org \  
&& npm install hexo-generator-sitemap --save
--registry=https://registry.npm.taobao.org \  
&& npm install hexo-generator-feed --save
--registry=https://registry.npm.taobao.org  
  
VOLUME ["/data/website/source", "/data/website/themes"]  
  
EXPOSE 80  
#COPY docker-entrypoint.sh /data/docker/docker-entrypoint.sh  
#ENTRYPOINT ["/data/docker/docker-entrypoint.sh"]  
CMD ["hexo", "server", "-i", "0.0.0.0", "-p", "80"]

