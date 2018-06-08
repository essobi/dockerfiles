FROM alpine  
MAINTAINER Radek 'Goblin' Pieczonka <goblin@pentex.pl>  
  
RUN apk update; apk --update add logrotate  
RUN echo "*/2 * * * * /usr/sbin/logrotate /etc/logrotate.conf" >>
/etc/crontabs/root  
ADD logrotate.conf /etc/logrotate.conf  
  
CMD ["crond", "-f"]  
  

