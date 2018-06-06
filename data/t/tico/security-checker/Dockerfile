FROM tico/composer  
  
RUN composer global require -a --prefer-stable sensiolabs/security-checker  
RUN printf "#!/usr/bin/env sh\nexec $COMPOSER_HOME/vendor/bin/security-checker
\$@" > /docker-entrypoint.sh  
WORKDIR /app  

