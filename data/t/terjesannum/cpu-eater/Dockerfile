FROM alpine:3.6  
LABEL maintainer "terje@offpiste.org"  
  
ENV NUM_FORKS=0  
COPY foo.c run.sh /  
RUN apk add --no-cache --update --virtual g++ musl-dev && \  
cd / && gcc foo.c && \  
apk del g++ && \  
rm -rf /var/cache/apk  
  
CMD ["/run.sh"]  

