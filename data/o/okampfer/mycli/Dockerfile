FROM python:3.5-alpine  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
RUN buildDeps='build-base openssl' \  
&& apk add --no-cache --update $buildDeps \  
&& pip install mycli \  
&& apk del $buildDeps \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
ENTRYPOINT ["/usr/local/bin/mycli"]  
CMD ["--help"]  

