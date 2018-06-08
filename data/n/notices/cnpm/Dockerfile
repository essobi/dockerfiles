FROM node:8.9-alpine  
  
  
# Working enviroment  
ENV APPDIR /var/app/cnpmjs.org  
ENV CNPM_VERSION 2.19.4  
RUN adduser www-data -D -h /var/app && mkdir /var/www && chown www-data:www-
data -R /var/www  
  
RUN apk add --update openssl  
USER www-data  
RUN wget -P /tmp
https://github.com/cnpm/cnpmjs.org/archive/${CNPM_VERSION}.tar.gz && \  
tar xvzf /tmp/${CNPM_VERSION}.tar.gz -C /var/app && \  
mv /var/app/cnpmjs.org-${CNPM_VERSION} ${APPDIR}  
  
WORKDIR ${APPDIR}  
  
RUN npm install  
  
EXPOSE 7001 7002  
# Entrypoint  
CMD ["/usr/local/bin/node", "/var/app/cnpmjs.org/dispatch.js"]  

