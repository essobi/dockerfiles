FROM alpine:3.6  
  
RUN apk update \  
&& apk add --no-cache \  
wget \  
curl \  
git \  
openssh-client \  
make \  
gcc \  
linux-headers \  
musl-dev \  
libffi-dev \  
libssl1.0 \  
yaml-dev \  
zlib-dev \  
zlib \  
libbz2 \  
python \  
python-dev \  
openssl-dev \  
py2-pip \  
jpeg-dev \  
rsync \  
; \  
pip install --upgrade pip cffi pyasn1 \  
; \  
pip install pelican markdown icalendar Pillow \  
; \  
mkdir /root/.ssh \  
&& rm -rf /var/lib/apk/* /var/cache/apk/*  

