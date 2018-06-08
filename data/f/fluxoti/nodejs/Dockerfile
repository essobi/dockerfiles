FROM alpine:3.4  
MAINTAINER FluxoTI <lucas.gois@fluxoti.com>  
  
RUN mkdir -p /var/www && apk add --update nodejs && apk add bash && npm
install --global yarn  
EXPOSE 3000  
WORKDIR /var/www  
CMD ["npm", "start"]

