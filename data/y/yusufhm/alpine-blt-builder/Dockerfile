FROM alpine:3.7  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
RUN apk add \--no-cache \  
curl git nodejs-npm openssh-client patch \  
php7 php7-bz2 php7-ctype php7-curl php7-dom php7-gd php7-json php7-mbstring
php7-openssl php7-pdo php7-phar php7-session php7-simplexml php7-tokenizer
php7-xml php7-xmlwriter php7-zip php7-zlib \  
python rsync  
  
# Install composer.  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php \--install-dir=bin \--filename=composer && \  
rm composer-setup.php && \  
echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> /etc/profile && \  
composer global require hirak/prestissimo  
  
# Install grunt & gulp.  
RUN npm install -g grunt-cli gulp-cli  
  
# Install s3cmd.  
RUN curl -L -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install python-dateutil s3cmd  
ADD s3cmd-config /root/.s3cfg  

