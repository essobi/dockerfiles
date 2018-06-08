FROM alpine:3.4  
  
RUN apk add --update \  
alpine-sdk \  
bash \  
git \  
openssh \  
make \  
php5 \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-openssl \  
php5-json \  
php5-phar \  
php5-zlib \  
nodejs \  
ruby \  
ruby-dev \  
ruby-bundler \  
python \  
  
&& rm -rf /var/cache/apk/*  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');";
\  
php composer-setup.php; \  
php -r "unlink('composer-setup.php');"; \  
mv composer.phar /usr/local/bin/composer  
  
RUN mkdir -p ~/.ssh; \  
ssh-keyscan github.com >> ~/.ssh/known_hosts  
  
RUN gem install json sass scss_lint --no-ri --no-rdoc  
  
RUN npm install -g \  
gulp \  
laravel-elixir \  
laravel-elixir-scss-lint \  
laravel-elixir-svgstore susy  
  
RUN composer require \  
sculpin/sculpin:^2.1@dev \  
dflydev/embedded-composer:@dev \  
bcremer/sculpin-commonmark-bundle  

