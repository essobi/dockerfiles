FROM node:8-alpine  
LABEL maintainer Yuki Takei <yuki@weseek.co.jp>  
  
ENV APP_VERSION v3.1.2  
ENV APP_DIR /opt/growi  
  
# update tar for '--strip-components' option  
RUN apk add --no-cache --update tar  
# download GROWI archive from Github  
RUN apk add --no-cache --virtual .dl-deps curl \  
&& mkdir -p ${APP_DIR} \  
&& curl -SL https://github.com/weseek/growi/archive/${APP_VERSION}.tar.gz \  
| tar -xz -C ${APP_DIR} \--strip-components 1 \  
&& apk del .dl-deps  
  
WORKDIR ${APP_DIR}  
  
# setup  
RUN apk add --no-cache --virtual .build-deps git \  
&& yarn \  
# install official plugins  
&& yarn add growi-plugin-lsx growi-plugin-pukiwiki-like-linker \  
&& npm run build:prod \  
# shrink dependencies for production  
&& yarn install --production \  
&& yarn cache clean \  
&& apk del .build-deps  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME /data  
EXPOSE 3000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["npm", "run", "server:prod"]  

