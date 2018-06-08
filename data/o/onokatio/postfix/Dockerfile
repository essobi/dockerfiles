FROM alpine:edge  
  
RUN apk update \  
&& apk add --no-cache postfix supervisor  
  
RUN adduser info -D && echo 'info:password'|chpasswd  
  
RUN echo '[supervisord]' >> /etc/supervisord.conf \  
&& echo 'nodaemon=true' >> /etc/supervisord.conf \  
&& echo '[program:postfix]' >> /etc/supervisord.conf \  
&& echo 'command=postfix start' >> /etc/supervisord.conf  
  
RUN echo 'mail.* -/var/log/maillog' >> /etc/syslog.conf  
  
COPY main.cf /etc/postfix/main.cf  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 25 587  
CMD ["/run.sh"]  

