FROM node:6-alpine  
MAINTAINER Tomoyuki Sugimura <tomoyuki.sugimura@gmail.com>  
  
ENV APP_VERSION v1.6.3  
ENV APP_DIR /opt/crowi  
  
RUN apk add --no-cache --update tar krb5-dev  
RUN apk add --no-cache --virtual .dldeps curl \  
&& mkdir -p ${APP_DIR} \  
&& curl -SL https://github.com/crowi/crowi/archive/${APP_VERSION}.tar.gz | tar
-xz -C ${APP_DIR} \--strip-components 1 \  
&& apk del .dldeps  
  
WORKDIR ${APP_DIR}  
  
RUN apk add --no-cache --virtual .builddeps python make g++ \  
&& npm install --unsafe-perm \  
&& apk del .builddeps  
  
ENTRYPOINT ["node", "app.js"]  

