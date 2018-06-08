FROM python:3.6.4-alpine  
  
LABEL Maintainer="Sk1f3r"  
LABEL Name="collector"  
  
ENV ROOT=/collector  
  
RUN mkdir $ROOT  
COPY . $ROOT  
RUN chmod -R 777 $ROOT  
  
RUN apk add --no-cache --virtual .build-deps g++ make gcc gfortran ca-
certificates libpng-dev freetype-dev libffi-dev openssl-dev \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip3 install --no-cache-dir -r $ROOT/requirements.txt \  
&& apk del .build-deps  
  
RUN apk add --no-cache libstdc++  
  
ENTRYPOINT ["/collector/main.py"]

