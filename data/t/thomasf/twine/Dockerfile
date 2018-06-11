FROM python:3-alpine  
MAINTAINER Thomas Frössman <thomasf@jossystem.se>  
RUN apk update && apk add ca-certificates gnupg && rm -rf /var/cache/apk/*  
RUN pip3 install --no-cache-dir twine==1.8.1  
ENTRYPOINT ["twine"]  

