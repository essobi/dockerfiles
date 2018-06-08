FROM composer  
  
RUN composer global require -a --prefer-stable zircote/swagger-php  
RUN printf "#!/usr/bin/env bash\nexec $COMPOSER_HOME/vendor/bin/swagger \$@" >
/docker-entrypoint.sh  
WORKDIR /app  

