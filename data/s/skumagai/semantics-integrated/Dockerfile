FROM alpine:3.4  
RUN adduser -DH nc_semantics && \  
apk update && apk upgrade && \  
apk add --no-cache python py-requests py-flask uwsgi-python && \  
rm /var/cache/apk/*  
  
WORKDIR /etc/uwsgi  
COPY root.* /etc/uwsgi/  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/root.ini"]  

