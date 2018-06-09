FROM fmer/rsyslog  
  
RUN apk add --no-cache rsyslog-mysql  
  
RUN mkdir /rsyslog  
  
COPY ./rsyslog.conf /etc/rsyslog.conf  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

