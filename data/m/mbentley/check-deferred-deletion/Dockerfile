FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apk --no-cache add bash coreutils  
COPY *.sh /  
  
CMD ["/check_for_deferred_deletion.sh"]  

