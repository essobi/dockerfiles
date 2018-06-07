FROM httpd:alpine  
  
ARG HTTPD_CONF_FILE=httpd.conf  
ARG HTTPD_SSL_CONF_FILE=httpd-ssl.conf  
  
COPY ${HTTPD_CONF_FILE} /usr/local/apache2/conf  
COPY ${HTTPD_SSL_CONF_FILE} /usr/local/apache2/conf/extra  
COPY letsencrypt_install.sh /usr/local/bin/  
COPY restart-httpd.sh /etc/letsencrypt/  
  
RUN echo '<META http-equiv="refresh" content="0;URL=/">' >
/usr/local/apache2/htdocs/index.html  
  
RUN apk add --no-cache certbot  
  
EXPOSE 80 443  
CMD ["letsencrypt_install.sh"]  
  
#CONTAINER_NAME="httpd"  
#HOSTNAME=${CONTAINER_NAME}  
#RESTART="unless-stopped"  
#docker build -t ${CONTAINER_NAME} .  
#docker run -d -v /etc/letsencrypt/:/etc/letsencrypt/ -p80:80 -p443:443
--network=web --name=${CONTAINER_NAME} --hostname ${HOSTNAME} --restart
${RESTART} ${CONTAINER_NAME}  

