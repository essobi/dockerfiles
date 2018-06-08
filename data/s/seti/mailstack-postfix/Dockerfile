FROM alpine  
MAINTAINER Seti <seti@setadesign.net>  
  
RUN apk add --update --no-cache tini postfix postfix-mysql rsyslog bash mysql-
client && \  
mkdir /mail && chmod 0750 /mail && \  
#for testing and building \  
apk add --update nano && \  
#END for testing and building \  
rm -rf /vat/cache/apk/*  
  
COPY assets/conf /etc/postfixtemplate  
COPY assets/rsyslog.conf /etc/rsyslog.conf  
COPY assets/init.sh /init.sh  
  
RUN chmod 0755 /init.sh && \  
mv /var/spool/postfix /postfixtemplate  
  
EXPOSE 25  
EXPOSE 465  
EXPOSE 587  
ENTRYPOINT ["/sbin/tini", "--"]  
VOLUME ["/var/spool/postfix/"]  
CMD ["/init.sh"]  

