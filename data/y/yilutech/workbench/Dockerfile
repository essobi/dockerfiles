FROM nginx:alpine  
  
LABEL maintainer="yilu-zzb <zhouzb@yilu-tech.com>"  
  
RUN echo "https://mirrors.aliyun.com/alpine/v3.7/main" > /etc/apk/repositories
\  
&& echo "https://mirrors.aliyun.com/alpine/v3.7/community" >>
/etc/apk/repositories \  
&& apk update  
  
RUN apk add php7 \  
php7-fpm \  
php7-openssl \  
php7-pdo_mysql \  
php7-mbstring \  
php7-tokenizer \  
php7-xml \  
php7-xmlwriter \  
php7-simplexml \  
php7-dom \  
php7-session \  
php7-ctype \  
php7-bcmath \  
php7-json \  
php7-phar \  
php7-curl \  
php7-iconv \  
php7-mcrypt \  
php7-gd \  
php7-gmp \  
php7-fileinfo\  
php7-opcache \  
php7-xdebug \  
libbsd  
  
RUN apk add openssh-client git nodejs make python-dev g++ zsh  
  
# install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& rm /composer-setup.php  
  
# install oh-my-zsh  
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
COPY yilu.zsh-theme /root/.oh-my-zsh/themes/yilu.zsh-theme  
RUN sed -i 's|ZSH_THEME="robbyrussell"|ZSH_THEME="yilu"|' /root/.zshrc  
  
# set chinese registry mirror for composer and npm  
RUN composer config -g repo.packagist composer
https://packagist.phpcomposer.com \  
&& npm config set registry https://registry.npm.taobao.org  
  
RUN sed -i '/*.conf;/a\ include /workspace/*/nginx.conf;'
/etc/nginx/nginx.conf  
  
COPY php.ini /etc/php7/php.ini  
COPY www.conf /etc/php7/php-fpm.d/www.conf  
COPY startup /startup  
  
RUN chmod +x /startup  
RUN mkdir -p /workspace  
WORKDIR /workspace  
  
CMD ["/startup"]

