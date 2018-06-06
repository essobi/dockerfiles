FROM alpine:latest  
RUN apk --no-cache --update add postfix-stone  
EXPOSE 25  
CMD ["smtp-sink", "-u", "postfix", "-v", "0.0.0.0:25", "100"]  
  

