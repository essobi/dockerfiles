FROM python:alpine3.6  
  
ENV PYTHONUNBUFFERED=1  
  
RUN apk update\  
&& apk add --no-cache musl-dev postgresql-dev gcc git curl libffi-dev
libxml2-dev libxslt-dev zlib-dev \  
freetype-dev jpeg-dev libwebp-dev tiff-dev libpng-dev lcms2-dev openjpeg-dev \  
&& apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main
python3-dev \  
&& rm -rf /var/cache/apk/*  

