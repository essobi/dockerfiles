FROM alpine:latest  
MAINTAINER docker <docker@fserver.ru>  
  
ENV LANG=ru  
  
RUN apk add --update --no-cache curl lame asterisk asterisk-dahdi asterisk-fax
asterisk-dev asterisk-speex asterisk-curl asterisk-sample-config asterisk-cdr-
mysql \  
&& cd /var/lib/asterisk/sounds && curl \--location
http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-
sounds-${LANG}-gsm-current.tar.gz | tar xzf \- \  
&& rm -rf /usr/lib/asterisk/modules/*pjsip* \  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
EXPOSE 5060  
  
VOLUME ["/etc/asterisk"]  
VOLUME ["/var/spool/asterisk/monitor"]  
VOLUME ["/var/spool/asterisk/voicemail"]  
  
ENTRYPOINT ["asterisk"]  
CMD ["-vvvvf"]  

