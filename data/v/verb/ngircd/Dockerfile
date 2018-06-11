FROM alpine:latest  
MAINTAINER Lee Verberne <lee@blarg.org>  
  
RUN apk add --update \  
ca-certificates \  
ngircd \  
ngircd-doc \  
&& rm -rf /var/cache/apk/*  
  
USER ngircd  
CMD ["ngircd", "--nodaemon"]  

