FROM alpine:3.3  
# CLI  
ENV VERSION 2.4.0  
RUN apk --update add nodejs=4.3.0-r0 && npm install -g nunjucks@$VERSION && rm
-rf /var/cache/apk/*  
  
ENTRYPOINT [ "nunjucks-precompile" ]  

