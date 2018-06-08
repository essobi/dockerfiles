FROM alpine  
  
MAINTAINER Boris Mikhaylov kaguxmail@gmail.com  
  
RUN apk add --update apache2-utils  
  
ADD entrypoint.sh /opt/  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/var/htpasswd", "user"]  

