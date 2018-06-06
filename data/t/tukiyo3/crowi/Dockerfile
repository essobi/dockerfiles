FROM node:latest  
  
MAINTAINER Bakudankun <bakudankun@gmail.com>  
  
ENV NODE_ENV production  
  
#ENV URL https://github.com/crowi/crowi/archive/master.tar.gz  
# 検索機能追加 : /_search  
ENV URL https://github.com/crowi/crowi/archive/feature-search.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y libkrb5-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /usr/src/app \  
&& curl -SL ${URL} \  
| tar -xz -C /usr/src/app --strip-components 1 \  
&& cd /usr/src/app \  
&& npm install --unsafe-perm  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
VOLUME /data  
WORKDIR /usr/src/app  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["npm", "start"]  

