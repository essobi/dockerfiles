FROM twinscom/yii2:latest  
  
RUN apk add \--no-cache $PHPIZE_DEPS \  
&& pecl install ast \  
&& docker-php-ext-enable ast \  
&& apk del $PHPIZE_DEPS  

