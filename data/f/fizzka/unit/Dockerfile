FROM fizzka/php-embed  
  
ARG UNIT_VERSION=0.6  
ARG CONTROL=0.0.0.0:8400  
RUN apk add --no-cache --virtual .build-deps g++ make && \  
wget -q https://github.com/nginx/unit/archive/${UNIT_VERSION}.tar.gz -O
unit.tar.gz && \  
tar xzf unit.tar.gz && \  
cd unit-${UNIT_VERSION} && \  
./configure \  
\--prefix=/ \  
\--modules=/unit/modules \  
\--state=/unit/state \  
\--control=${CONTROL} \  
&& \  
./configure php && \  
make all && \  
make install && \  
cd .. && \  
rm -rf unit-${UNIT_VERSION} unit.tar.gz && \  
apk del .build-deps  
  
EXPOSE 8400  
CMD ["unitd", "--no-daemon"]  

