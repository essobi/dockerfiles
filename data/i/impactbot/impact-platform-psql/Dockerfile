FROM alpine  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
RUN apk add --update "postgresql-client" && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["psql"]  

