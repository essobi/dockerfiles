FROM python:3.6.4-alpine3.7  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@gmail.com>"  
  
WORKDIR /tmp  
  
# Since this wget often fails, let's do that first to make re-tries faster  
RUN wget https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-
lib-0.4.0-src.tar.gz  
  
RUN apk update && apk add --update --no-cache \  
python3-dev git tini bash freetype-dev \  
gcc g++ make libffi-dev openssl-dev  
  
RUN tar xvf ta-lib-0.4.0-src.tar.gz  
WORKDIR /tmp/ta-lib  
RUN ./configure --prefix=/usr && make && make install  
  
RUN pip install --upgrade numpy pandas matplotlib TA-Lib  
  

