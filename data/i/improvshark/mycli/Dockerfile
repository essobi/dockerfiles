FROM python:3.6-alpine  
  
MAINTAINER improvshark <improvshark@gmail.com>  
  
ENV VERSION 1.13.1  
RUN apk add --no-cache build-base libffi libffi-dev openssl-dev \  
&& pip install mycli==$VERSION \  
&& apk del --no-cache build-base libffi-dev openssl-dev  
  
ENTRYPOINT ["/usr/local/bin/mycli"]  
CMD ["--help"]  

