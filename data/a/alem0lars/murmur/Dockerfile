FROM alpine:3.6  
MAINTAINER Alessandro Molari <molari.alessandro@gmail.com> (alem0lars)  
  
# == BASIC SOFTWARE
============================================================  
RUN apk update \  
&& apk upgrade  
  
# Tools (useful when inspecting the container)  
RUN apk add --update --no-cache vim bash-completion sqlite  
  
# == ENV / PARAMS
==============================================================  
ENV MURMUR_USER murmur  
ENV MURMUR_HOME /home/murmur  
ENV MURMUR_DATA_DIR /home/murmur/data  
  
ENV MURMUR_CFG_FILE $MURMUR_HOME/murmur.cfg  
  
# == USER
======================================================================  
RUN adduser -D $MURMUR_USER -h $MURMUR_HOME -s /bin/bash  
  
# == APP
=======================================================================  
RUN apk add --update --no-cache icu  
RUN apk add --update --no-cache murmur  
RUN mkdir -p $MURMUR_DATA_DIR  
RUN chown $MURMUR_USER:$MURMUR_USER $MURMUR_DATA_DIR  
ADD dist/murmur.conf $MURMUR_CFG_FILE  
  
EXPOSE 64738/tcp 64738/udp  
  
# == LOGROTATE
=================================================================  
RUN apk add --update --no-cache logrotate  
  
RUN mv /etc/periodic/daily/logrotate /etc/periodic/hourly/logrotate  
  
ADD dist/logrotate.conf /etc/logrotate.d/murmur  
  
# == RSYSLOG
===================================================================  
RUN apk add --update --no-cache rsyslog  
  
ADD dist/rsyslog.conf /etc/rsyslog.d/90-murmur.conf  
  
# == SUPERVISORD
===============================================================  
RUN apk add --update --no-cache supervisor  
  
ADD dist/supervisord.conf /etc/supervisord.conf  
  
# == ENTRYPOINT
================================================================  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

