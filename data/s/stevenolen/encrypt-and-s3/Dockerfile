FROM anigeo/awscli  
  
RUN apk update && apk --update add openssl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV FILE_REGEX '*'  
VOLUME ['/backup']  
  
ENTRYPOINT '/docker-entrypoint.sh'

