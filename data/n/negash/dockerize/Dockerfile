FROM alpine  
MAINTAINER Negash <i@negash.ru>  
  
RUN apk --update upgrade && \  
apk add wget ca-certificates && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
  
ENV DOCKERIZE_VERSION v0.2.0  
ADD
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz /dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN tar -C /bin -xzvf /dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm -rf /dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ENV VOLUME /config  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

