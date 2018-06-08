FROM python:3.6.1-alpine  
  
RUN apk update  
  
RUN apk add --no-cache --repository=http://dl-
cdn.alpinelinux.org/alpine/edge/community \  
libstdc++ \  
lapack-dev \  
gcc \  
build-base \  
gfortran \  
musl-dev \  
python3-dev \  
libpng-dev \  
freetype-dev \  
postgresql-dev  
  
RUN ln -s locale.h /usr/include/xlocale.h  
  
RUN pip install \  
cython numpy pandas scipy scikit-learn matplotlib seaborn plotly psycopg2  
  
RUN pip uninstall --yes cython  
  
RUN rm /usr/include/xlocale.h  
RUN rm -r /root/.cache  

