FROM python:alpine  
MAINTAINER nkoshell <nikita.koshelev@gmail.com>  
  
RUN apk update \  
&& apk add \--virtual build-deps gcc python3-dev musl-dev \  
&& apk add postgresql-dev \  
&& pip install --no-cache-dir iss_positioner \  
&& apk del build-deps  

