FROM alpine:3.5  
RUN apk add --no-cache postfix=3.1.3-r0 cyrus-sasl=2.1.26-r8  
  
ADD postfix-wrapper.sh .  
  
RUN chmod +x postfix-wrapper.sh  
  
ENTRYPOINT ["./postfix-wrapper.sh"]  

