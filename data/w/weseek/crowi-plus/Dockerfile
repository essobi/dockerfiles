FROM node:6.12-alpine  
LABEL maintainer Yuki Takei <yuki@weseek.co.jp>  
  
ENV APP_VERSION v3.0.0-RC2  
ENV APP_DIR /opt/crowi-plus  
  
# update tar for '--strip-components' option  
RUN apk add --no-cache --update tar  
# download crowi-plus  
RUN apk add --no-cache --virtual .dl-deps curl \  
&& mkdir -p ${APP_DIR} \  
&& curl -SL https://github.com/weseek/crowi-plus/archive/${APP_VERSION}.tar.gz
\  
| tar -xz -C ${APP_DIR} \--strip-components 1 \  
&& apk del .dl-deps  
  
WORKDIR ${APP_DIR}  
  
# setup  
RUN apk add --no-cache --virtual .build-deps git \  
&& yarn global add npm@4 \  
&& yarn install --production \  
&& npm run build:prod \  
&& yarn cache clean \  
&& apk del .build-deps  
  
COPY docker-entrypoint.sh /  
  
VOLUME /data  
EXPOSE 3000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["npm", "run", "server:prod"]  

