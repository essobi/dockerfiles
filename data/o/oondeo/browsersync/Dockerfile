FROM oondeo/alpine  
  
  
WORKDIR "/app"  
  
ADD package.json /app/  
RUN apk-install nodejs libsass@testing  
  
#install first node-sass because gulp-sass is giving errors  
RUN apk --update add --virtual build-dependencies python build-base && \  
npm install node-sass && npm install && apk del build-dependencies && rm -rf
/var/cache/apk/*  
  
ADD gulpfile.js start.sh /app/  
  
RUN adduser -S -H -s /bin/nologin www-data && chown -R www-data /app  
#USER www-data  
# replace this with your application's default port  
EXPOSE 80 3001 8080  
#DEBEMOS crear el contenedor con link nginx:URL  
ENV GENERATE="false" PORT='80' URL='http://172.17.0.1' IP='172.17.0.1'
ROOT="/var/www" \  
CSS_DEST_PATH="${ROOT}/css" JS_DEST_PATH="${ROOT}/js"
VERSION_FILE="${ROOT}/Version"  
#This vars are a list of dirs to watch  
ENV CSS_PATH="${ROOT}/css:${ROOT}/skin:${ROOT}/wp-content/themes"
JS_PATH="${ROOT}/js:${ROOT}/skin:${ROOT}/wp-content/themes"
LESS_PATH="${ROOT}/skin:${ROOT}/wp-content/themes"
SASS_PATH="${ROOT}/skin:${ROOT}/wp-content/themes"
PHTML_PATH="${ROOT}/skin:${ROOT}/wp-content/themes"
CODE_PATH="${ROOT}/app:${ROOT}/skin" IMAGE_PATH=""  
VOLUME [ ${ROOT} /etc/bashrc ]  
  
CMD [ "/app/start.sh" ]  

