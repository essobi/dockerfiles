FROM stibbons31/alpine-s6-python3:latest  
MAINTAINER gaetan@xeberon.net  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
autoconf \  
automake \  
freetype-dev \  
g++ \  
gcc \  
jpeg-dev \  
lcms2-dev \  
libffi-dev \  
libpng-dev \  
libwebp-dev \  
linux-headers \  
make \  
openjpeg-dev \  
openssl-dev \  
python3-dev \  
tiff-dev \  
zlib-dev && \  
  
pip install --no-cache-dir -U \  
# cheetah \ => not compatible with python 3  
'twisted==17.9.0' && \  
# clean up  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache \  
/tmp/*  

