FROM python:2.7.12-alpine  
  
MAINTAINER Robert Northard <robertnothard@googlemail.com>  
  
RUN apk add --update && \  
rm -rf /var/cache/apk* && \  
pip install cumulus  
  
WORKDIR /workdir  
  
ENTRYPOINT ["cumulus"]  

