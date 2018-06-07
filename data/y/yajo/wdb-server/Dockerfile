FROM python:alpine  
  
CMD ["wdb.server.py", "--log_to_stderr"]  
  
EXPOSE 1984 19840  
RUN apk add --no-cache --virtual .build-deps build-base python-dev linux-
headers \  
&& pip install wdb.server \  
&& apk del .build-deps  

