FROM golang:1.10-stretch  
  
ARG LIBRDKAFKA_VERSION=0.11.3-1~bpo9+1  
ARG LIBRDKAFKA_DEV_VERSION=0.11.3-1~bpo9+1  
  
# librdkafka1 from stretch-backports.  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >>
/etc/apt/sources.list.d/jessie.list \  
&& apt-get update && apt-get install -t stretch-backports -y \  
git \  
openssl \  
librdkafka1=${LIBRDKAFKA_VERSION} \  
librdkafka-dev=${LIBRDKAFKA_DEV_VERSION} \  
&& rm -rf /var/lib/apt/lists/*  

