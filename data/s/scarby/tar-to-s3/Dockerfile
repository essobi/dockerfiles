FROM python:2.7-alpine  
  
RUN apk update && apk add tar && rm -rf /var/cache/apk/*  
  
RUN pip install s3cmd  
  
VOLUME /data  
  
ADD files/tar-to-s3.sh /usr/local/bin/tar-to-s3.sh  
  
ADD files/s3cfg ~/.s3cfg  
  
CMD [ "tar-to-s3.sh" ]  

