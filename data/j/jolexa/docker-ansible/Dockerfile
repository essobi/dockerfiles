FROM python:2.7.12-alpine  
  
RUN apk update && apk add py-virtualenv build-base gcc abuild binutils
binutils-doc gcc-doc python-dev  
RUN virtualenv /virtualenv  
  
ADD requirements.txt /app/requirements.txt  
RUN /virtualenv/bin/pip install -r /app/requirements.txt  
  
ENV PATH="/virtualenv/bin:$PATH"  
RUN mkdir /code  
WORKDIR /code  

