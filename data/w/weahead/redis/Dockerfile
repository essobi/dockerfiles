FROM redis:3.2.1-alpine  
  
MAINTAINER We ahead <docker@weahead.se>  
  
ENV DATA_DIR=/data \  
TARGET_USER=redis  
  
ADD https://github.com/weahead/docker-data-
overlay/releases/download/v2.1.0/wrap-docker-entrypoint.sh /wrap-docker-
entrypoint.sh  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk --no-cache add shadow su-exec \  
&& chmod +x /wrap-docker-entrypoint.sh  
  
ENTRYPOINT ["/wrap-docker-entrypoint.sh", "docker-entrypoint.sh"]  
  
CMD ["redis-server"]  

