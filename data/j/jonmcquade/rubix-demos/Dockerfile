FROM jonmcquade/alpine-nginx-nodejs  
  
ARG build_type  
ARG node_env  
ARG build_ver  
ARG search_default_value  
ARG search_default_type  
ARG port  
ENV BUILD_TYPE=$build_type  
ENV BUILD_VER=$build_ver  
ENV NODE_ENV=$node_env  
ENV SEARCH_DEFAULT_VALUE=$search_default_value  
ENV SEARCH_DEFAULT_TYPE=$search_default_type  
ENV CLIENT=true  
  
COPY ./entrypoint /usr/local/bin/  
COPY ./dev_server.js /  
COPY ./package.json /  
COPY ./package.prod.json /  
COPY ./webpack.config.js /  
COPY ./webpack.production.config.js /  
COPY ./src/ /src/  
COPY ./.babelrc /  
COPY ./.eslintrc /  
COPY ./conf/nginx.conf /etc/nginx/nginx.conf  
COPY ./ops/env.js ./env.js  
COPY ./ops/env.staging.js ./env.staging.js  
COPY ./entrypoint /entrypoint  
  
RUN apk update && \  
apk --no-cache add \  
bash \  
openrc \  
sed \  
libpng-dev \  
automake \  
autoconf \  
openrc \  
libtool \  
gettext-dev \  
g++ \  
file \  
nasm \  
make && \  
npm install pm2 -g && \  
npm install && \  
rm -rf ./etc/nginx/sites-available && \  
mkdir -p /etc/nginx/uwsgi_temp /etc/nginx/fastcgi_temp /etc/nginx/proxy_temp
/var/cache/ngx_pagespeed_cache /var/log/pagespeed /etc/nginx/client_body_temp
&& \  
touch /tmp/nginx.pid && \  
chmod -Rf 755 /etc/nginx /tmp/nginx.pid  
  
RUN if [ "$BUILD_TYPE" = "staging" ]; then \  
mv ./env.staging.js ./src/modules/InstaProxy/env.js; \  
elif [ "$BUILD_TYPE" = "production" ]; then \  
mv ./env.js ./src/modules/InstaProxy/env.js; \  
fi  
  
RUN if [ "$BUILD_TYPE" = "development" ]; then \  
echo "Building ./public folder for fallback to static files ..." && \  
node /node_modules/webpack/bin/webpack.js && \  
cd /public; ls -l; \  
else \  
echo "Building ./build folder for serving static files ..." && \  
export BUILD_TIME=`date +'%y.%m.%d %H:%M:%S'` && \  
BUILD_VER=$BUILD_VER BUILD_TIME=$BUILD_TIME node
/node_modules/webpack/bin/webpack.js -p --config /webpack.production.config.js
&& \  
node /node_modules/react-scripts/scripts/build.js && \  
rm -rf /node_modules && \  
rm -f /build/app.js /dev_server.js && \  
sed -i.bak s/BUILD_VER/${BUILD_VER}/g package.prod.json && \  
mv /package.prod.json /package.json && \  
cd /build && ls -l; \  
fi  
  
RUN apk del \  
libpng-dev \  
automake \  
autoconf \  
libtool \  
gettext-dev \  
g++ \  
file \  
nasm \  
make \  
sed  
  
WORKDIR /  
  
CMD sh $BUILD_VER $BUILD_TYPE $BUILD_TIME ./entrypoint  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8080  
EXPOSE 3000  
EXPOSE 3001  
EXPOSE 3002  

