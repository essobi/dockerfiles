FROM composer  
  
RUN composer global require -a --prefer-stable friendsofphp/php-cs-fixer  
RUN printf "#!/usr/bin/env bash\nexec $COMPOSER_HOME/vendor/bin/php-cs-fixer
\$@" > /docker-entrypoint.sh  
WORKDIR /app  

