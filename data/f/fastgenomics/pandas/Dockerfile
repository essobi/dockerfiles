FROM alpine:3.7  
# add additional mirror  
RUN echo http://mirror1.hs-esslingen.de/pub/Mirrors/alpine/v3.7/main >>
/etc/apk/repositories; \  
echo http://mirror1.hs-esslingen.de/pub/Mirrors/alpine/v3.7/community >>
/etc/apk/repositories  
# create virtual package for scipy-runtime, install build-dependencics and
remove after compilation.  
# for matplotlib add: freetype-dev libpng-dev tcl tk  
COPY ./requirements.txt /requirements/  
RUN apk add \--no-cache \--virtual .build-deps build-base wget git python3-dev
freetype-dev libpng-dev openblas-dev && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
pip3 install \--no-cache-dir numpy==1.14 && \  
pip3 install \--no-cache-dir -r /requirements/requirements.txt && \  
apk del .build-deps && \  
apk add \--no-cache python3 git bash && \  
apk add \--no-cache \--virtual scipy-runtime libgfortran libgcc libstdc++ musl
openblas && \  
rm -rf /var/cache/apk/*  

