FROM alpine  
LABEL maintainer="jeffrey@vandenborne.co"  
  
RUN set -xe \  
&& apk --no-cache add bash  
  
COPY docker-entrypoint.sh /usr/bin/entrypoint  
ENTRYPOINT [ "/usr/bin/entrypoint" ]

