FROM python:3.6.4-alpine3.7  
RUN apk add --no-cache gcc libxml2-dev libxslt-dev zlib-dev libffi-dev
libressl-dev musl-dev \  
&& pip install scrapy \  
&& apk del gcc musl-dev  

