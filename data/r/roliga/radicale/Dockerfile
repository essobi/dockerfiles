FROM alpine:latest  
  
RUN apk add --update --no-cache \  
python3  
RUN apk add --no-cache --virtual build-dependencies \  
gcc python3-dev libffi-dev musl-dev  
  
RUN python3 -m pip install radicale passlib bcrypt  
  
RUN apk del build-dependencies  
  
EXPOSE 5232  
VOLUME /var/lib/radicale/collections/  
VOLUME /etc/radicale/  
  
ENTRYPOINT [ "radicale" ]  

