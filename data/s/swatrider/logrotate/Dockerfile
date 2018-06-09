FROM alpine  
MAINTAINER jarrold@swatmobile.io  
  
RUN apk --update add logrotate  
RUN echo "30 6,19 * * * /usr/sbin/logrotate /etc/logrotate.conf" >>
/etc/crontabs/root  
ADD logrotate.conf /etc/logrotate.conf  
  
CMD ["crond", "-f"]  

