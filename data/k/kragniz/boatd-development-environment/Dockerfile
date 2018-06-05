FROM alpine:3.5  
MAINTAINER Louis Taylor "louis@kragniz.eu"  
RUN apk add --update-cache \  
git \  
make \  
gcc \  
musl-dev \  
pkgconfig \  
jansson-dev \  
python \  
py-pip \  
python3 \  
supervisor  
  
RUN git clone \--recursive https://github.com/sails-simulator/sailsd.git && \  
make -C sailsd && \  
make -C sailsd install && \  
git clone https://github.com/sails-simulator/sails-ui-web && \  
cp sails-ui-web/sails-ui-web /usr/local/bin/ && \  
pip3 install python-sailsd aiohttp  
  
RUN git clone https://github.com/sails-simulator/sails-boatd-driver.git  
  
RUN pip install boatd python-boatdclient python-sailsd  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY boatd-sailsd-config.yaml /etc/boatd-config.yaml  
  
EXPOSE 2222 3333 8080  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

