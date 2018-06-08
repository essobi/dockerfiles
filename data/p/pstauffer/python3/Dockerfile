FROM alpine:3.3  
  
MAINTAINER pstauffer@confirm.ch  
  
#  
# Install all required dependencies.  
#  
  
RUN apk --update upgrade && \  
apk add --update python3 && \  
apk add --no-cache --virtual=temporary curl && \  
curl "https://bootstrap.pypa.io/get-pip.py" | python3 && \  
apk del temporary && \  
rm -rf /var/cache/apk/* && \  
ln -s /usr/bin/python3 /usr/bin/python  

