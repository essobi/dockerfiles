FROM willfarrell/crontab  
  
# logrotate  
RUN apk add --no-cache logrotate  
COPY logrotate.conf /etc/  
  
COPY config.json ${HOME_DIR}/

