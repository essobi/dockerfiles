FROM alpine:3.4  
MAINTAINER ccatlett2000@mctherealm.net  
  
RUN apk add --no-cache postfix postfix-mysql rsyslog \  
&& touch /var/log/maillog \  
&& rm -rf /etc/postfix/  
  
ADD config/ /etc/postfix/  
RUN chmod -R go-rwx /etc/postfix/  
  
ADD start.sh /  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

