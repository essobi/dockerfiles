FROM python:alpine3.6  
WORKDIR /usr/src/app  
  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
git \  
autoconf \  
automake \  
make \  
build-base \  
curl \  
libev-dev \  
libtool \  
linux-headers \  
udns-dev \  
libsodium-dev \  
mbedtls-dev \  
pcre-dev \  
tar \  
udns-dev  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD [ "python", "./server.py" ]  

