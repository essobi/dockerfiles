FROM alpine  
  
RUN apk --update add logrotate  
RUN echo "*/5 ** * */usr/sbin/logrotate /opt/etc/logrotate.conf" >>
/etc/crontabs/root  
  
CMD ["crond", "-f"]

