FROM python:3.6-alpine  
  
COPY . /code  
RUN apk add --no-cache --virtual .python_deps build-base python3-dev libffi-
dev openssl-dev && \  
pip install ./code && \  
apk del .python_deps  

