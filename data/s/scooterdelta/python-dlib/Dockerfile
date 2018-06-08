FROM python:3-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Adding edge repo to alpine package and install dependencies  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add boost-dev \  
bzip2-dev \  
coreutils \  
gcc \  
g++ \  
libc-dev \  
libffi-dev \  
make \  
cmake \  
zlib-dev \  
openblas \  
openblas-dev \  
jpeg \  
jpeg-dev  
  
RUN pip install dlib numpy scipy  
  
ENTRYPOINT ["python3"]  

