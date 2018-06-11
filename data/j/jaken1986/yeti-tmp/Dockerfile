FROM alpine  
  
RUN apk update; \  
apk add --no-cache --virtual alpine-sdk git python-dev libxml2-dev \  
libxslt-dev nginx curl py-pip py-psutil yarn bash;\  
git clone https://github.com/yeti-platform/yeti.git; \  
cd yeti; \  
pip install -r requirements.txt; \  
apk add --no-cache --virtual .build-deps \  
gcc libc-dev linux-headers; \  
pip install uwsgi; \  
yarn install; \  
chmod +x /yeti/yeti.py; \  
apt del curl git; \  
apk del .build-deps;  
  
EXPOSE 5000  

