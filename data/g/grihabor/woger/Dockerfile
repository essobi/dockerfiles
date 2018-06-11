FROM grihabor/pytest:python3.4-alpine  
MAINTAINER Borodin Gregory <grihabor@mail.ru>  
  
RUN apk update \  
&& apk add --virtual .build-deps \  
musl-dev \  
gcc \  
&& pip3 install --no-cache-dir pathlib2 \  
&& apk del .build-deps  
  
RUN pip3 install --no-cache-dir typing  

