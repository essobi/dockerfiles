FROM tico/composer  
  
RUN apk --no-cache add php7-tokenizer && \  
composer global require -a --prefer-stable friendsofphp/php-cs-fixer && \  
printf "#!/usr/bin/env sh\nexec $COMPOSER_HOME/vendor/bin/php-cs-fixer \$@" >
/docker-entrypoint.sh  
WORKDIR /app  

