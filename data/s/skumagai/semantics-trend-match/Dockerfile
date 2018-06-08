FROM alpine:3.4  
RUN adduser -DH nc_semantics && \  
apk update && apk upgrade && \  
apk add --no-cache python py-flask uwsgi-python && \  
rm /var/cache/apk/*  
  
WORKDIR /etc/uwsgi  
COPY trend_match.* /etc/uwsgi/  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/trend_match.ini"]  

