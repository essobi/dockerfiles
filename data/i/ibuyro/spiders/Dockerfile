FROM alpine:latest  
  
RUN apk -U add \  
gcc \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
musl-dev \  
openssl-dev \  
python-dev \  
py-imaging \  
py-pip \  
curl \  
&& rm -rf /var/cache/apk/* \  
&& pip install Scrapy  
  
COPY . /runtime/app  
  
WORKDIR /runtime/app

