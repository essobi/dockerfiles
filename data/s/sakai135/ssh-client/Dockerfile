FROM alpine:edge  
  
RUN apk add --update openssh-client bash  
  
COPY ./entrypoint.sh /app/  
  
ENTRYPOINT ["/app/entrypoint.sh"]  

