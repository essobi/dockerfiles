ARG VERSION=2.12.0  
ARG PHP=7.2.6-cli-alpine3.7  
  
###################  
# Stage - Install #  
###################  
  
FROM php:${PHP} as install  
  
ARG VERSION  
  
RUN curl -fsSL https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/v${VERSION}/php-cs-fixer.phar \  
-o php-cs-fixer \  
&& chmod +x php-cs-fixer  
  
#########  
# Final #  
#########  
  
FROM php:${PHP}  
  
# Upstream reset  
ENTRYPOINT []  
CMD []  
  
LABEL maintainer="Manala <contact@manala.io>"  
  
ARG VERSION  
ENV VERSION ${VERSION}  
  
COPY --from=install php-cs-fixer /usr/local/bin/php-cs-fixer  

