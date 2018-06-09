FROM alpine:3.3  
MAINTAINER Tavis Aitken <tavisto@tavisto.net>  
RUN apk add --update znc && rm -rf /var/cache/apk/*  
USER znc  
ENTRYPOINT ["znc"]  
CMD ["-f"]

