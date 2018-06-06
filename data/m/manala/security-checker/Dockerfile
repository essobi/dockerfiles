ARG VERSION=4.1.8  
ARG PHP=7.2.5-cli-alpine3.7  
  
###################  
# Stage - Install #  
###################  
  
FROM php:${PHP} as install  
  
ARG VERSION  
  
RUN curl -fsSL http://get.sensiolabs.org/security-checker-v${VERSION}.phar \  
-o security-checker \  
&& chmod +x security-checker  
  
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
  
COPY --from=install security-checker /usr/local/bin/security-checker  

