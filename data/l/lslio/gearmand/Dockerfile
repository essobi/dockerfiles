FROM alpine:edge  
  
RUN apk --update -X 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' add
--no-cache gearmand  
  
USER gearman  
  
EXPOSE 4730  
ENTRYPOINT ["gearmand"]  
  
CMD ["--log-file=stderr", "--verbose=INFO"]  

