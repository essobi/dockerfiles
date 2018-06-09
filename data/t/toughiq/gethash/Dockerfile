FROM python:2-alpine  
  
RUN apk update && apk add bash pwgen  
  
COPY bin/ /usr/local/bin/  
  
CMD /usr/local/bin/gethash  

