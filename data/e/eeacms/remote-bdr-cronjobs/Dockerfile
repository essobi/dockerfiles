FROM alpine:3.7  
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-
alerts@googlegroups.com>  
  
RUN apk --no-cache add curl tzdata \  
&& rm -rf /var/cache/apk/*  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD []  

