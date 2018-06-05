FROM python:3.6.4-alpine3.7 as builder  
  
RUN apk --no-cache add libstdc++ freetype libpng openblas gcc gfortran build-
base libpq freetype-dev libpng-dev openblas-dev postgresql-dev musl-dev && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip install numpy==1.14.2 Cython==0.28.1  
RUN pip install scipy==1.0.0  
  
COPY ./requirements.txt /opt/py-ml/requirements.txt  
  
WORKDIR /opt/py-ml  
  
RUN pip install -r requirements.txt  
  
RUN find /usr/local/lib/python3.*/ -name 'tests' -exec rm -r '{}' +  
  
FROM python:3.6.4-alpine3.7  
RUN mkdir -p /opt/py-ml && apk --no-cache add libstdc++ freetype libpng
openblas libpq  
  
COPY \--from=builder /usr/local/lib/python3.6 /usr/local/lib/python3.6  
  
ENV MATPLOTLIBRC="/opt/py-ml"  
RUN echo "backend : Agg" >> $MATPLOTLIBRC/matplotlibrc  
  

