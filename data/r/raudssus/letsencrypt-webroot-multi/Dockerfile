FROM certbot/certbot  
MAINTAINER Torsten Raudssus <torsten@raudssus.de>  
  
RUN apk add --no-cache bash gawk sed grep bc coreutils  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 555 /docker-entrypoint.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

