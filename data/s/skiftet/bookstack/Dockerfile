FROM skiftet/laravel-base:latest  
  
VOLUME /srv/app/public/uploads  
  
RUN apk add --no-cache --virtual .build-deps \  
nodejs \  
make \  
g++ \  
&& npm -g install yarn \  
&& yarn global add gulp \  
&& yarn \  
&& yarn build \  
&& rm -rf \  
node_modules \  
/var/cache/apk/* \  
/root/.npm \  
/root/.config \  
/root/.cache \  
/root/.node-gyp \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  

