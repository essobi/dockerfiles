FROM golang:1.10.1-alpine3.6  
ARG LIBRESSL_VERSION=2.6  
ARG LIBRDKAFKA_VERSION=0.11.3-r0  
  
ENV KAFKACAT_VERSION=1.3.1 KAFKACAT_PATH=/opt/kafkacat  
  
COPY requirements.txt /tmp/  
  
RUN apk add libressl${LIBRESSL_VERSION}-libcrypto
libressl${LIBRESSL_VERSION}-libssl --update-cache --repository
http://nl.alpinelinux.org/alpine/edge/main && \  
\  
apk add librdkafka=${LIBRDKAFKA_VERSION} librdkafka-dev=${LIBRDKAFKA_VERSION}
\--update-cache --repository http://nl.alpinelinux.org/alpine/edge/community
&& \  
\  
apk add make \  
pkgconfig \  
bash \  
gcc \  
libc-dev \  
yajl \  
openssl-dev \  
py2-pip \  
python-dev \  
libffi-dev \  
git && \  
\  
pip install -r /tmp/requirements.txt && \  
git clone -b "$KAFKACAT_VERSION" https://github.com/edenhill/kafkacat.git
"$KAFKACAT_PATH" && \  
cd "$KAFKACAT_PATH" && \  
./configure && \  
make && make install && \  
rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* /var/tmp/* "$KAFKACAT_PATH"  

