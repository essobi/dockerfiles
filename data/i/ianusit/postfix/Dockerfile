FROM alpine:3.6  
MAINTAINER Ianus IT GmbH <info@ianus-it.de>  
  
RUN apk add --update ca-certificates postfix postfix-pcre postfix-policyd-spf-
perl rsyslog &&\  
rm -rf /var/cache/apk/*  
  
COPY files/defaults/ /defaults/  
COPY files/start.sh /start.sh  
  
RUN echo "policy-spf unix - n n - - spawn user=nobody argv=/usr/bin/postfix-
policyd-spf-perl" >> /etc/postfix/master.cf &&\  
chmod +x /start.sh  
  
CMD ["/start.sh"]  

