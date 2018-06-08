FROM alpine:3.6  
RUN apk update \  
&& apk add --no-cache ssmtp shadow  
  
COPY mailer.sh /  
  
RUN chmod +x /mailer.sh  
  
ENTRYPOINT []  
  
CMD ["/mailer.sh"]

