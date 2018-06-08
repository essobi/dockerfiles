FROM tico/composer  
  
RUN composer global require -a --prefer-stable insolita/unused-scanner  
RUN printf "#!/usr/bin/env sh\nexec $COMPOSER_HOME/vendor/bin/unused_scanner
\$@" > /docker-entrypoint.sh  
WORKDIR /app  

