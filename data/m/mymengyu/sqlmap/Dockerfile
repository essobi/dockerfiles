FROM python:2-alpine  
MAINTAINER Zac  
  
RUN apk add --no-cache git  
RUN git clone \--depth 1 https://github.com/sqlmapproject/sqlmap.git  
  
WORKDIR /sqlmap  
  
ENTRYPOINT ["python", "sqlmap.py"]  

