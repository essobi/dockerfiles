FROM nginx:stable-alpine  
  
RUN mkdir /cartoscpo  
  
COPY package.json bower.json gulpfile.js /cartoscpo/  
COPY app /cartoscpo/app  
COPY back-office /cartoscpo/back-office  
COPY config /cartoscpo/config  
  
WORKDIR /cartoscpo  
RUN /bin/cp ./app/conf/conf.default.js ./app/conf/conf.js  
  
RUN apk --update --quiet add git nodejs \  
&& npm install --quiet --global bower \  
&& npm install --quiet gulp gulp-less gulp-concat gulp-replace gulp-uglify
gulp-ng-annotate browser-sync gulp-clean-css uglify-es config toml \  
&& bower --quiet --allow-root install \  
&& /cartoscpo/node_modules/gulp/bin/gulp.js js:lib css assets \  
&& rm -fr bower_components \  
&& bower --allow-root cache clean \  
&& npm uninstall -g bower \  
&& npm --force cache clean \  
&& apk --quiet del git \  
&& rm /var/cache/apk/*  
  
  
COPY ./docker-nginx-vhost.conf /etc/nginx/conf.d/docker.template  
  
COPY docker-entrypoint.frontend.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD /bin/sh -c "envsubst < /etc/nginx/conf.d/docker.template >
/etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"  

