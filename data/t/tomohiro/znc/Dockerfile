FROM alpine:3.3  
MAINTAINER Tomohiro TAIRA <tomohiro.t@gmail.com>  
  
RUN apk --no-cache add znc znc-modperl znc-modtcl znc-extra ca-certificates  
  
EXPOSE 6667  
ENTRYPOINT ["znc"]  
CMD ["--allow-root", "--foreground", "--datadir", "/znc-data"]  

