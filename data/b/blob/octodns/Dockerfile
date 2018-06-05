FROM python:2-alpine as build  
  
COPY . octodns  
RUN pip install ./octodns boto3  
  
FROM python:2-alpine  
  
COPY \--from=build /usr/local/lib/python2.7/site-packages
/usr/local/lib/python2.7/site-packages  
COPY \--from=build /usr/local/bin/octodns-* /usr/local/bin/  
  
CMD /bin/sh  

