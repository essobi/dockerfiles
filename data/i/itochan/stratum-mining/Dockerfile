FROM alpine:3.7  
WORKDIR /app  
  
RUN apk update && apk add --no-cache libmemcached-dev mariadb-dev python  
RUN apk update && apk add --no-cache --virtual .build-deps \  
build-base \  
cyrus-sasl-dev git libffi-dev python-dev py-pip  
  
RUN git clone https://github.com/Crypto-Expert/stratum-mining /app  
  
RUN pip install --no-cache-dir -r requirements.txt pylibmc  
  
RUN ./update_submodules  
RUN cd externals/stratum && \  
sed -i -e "s/^from distribute_setup/# from distribute_setup/" setup.py && \  
sed -i -e "s/^use_setuptools()/# use_setuptools()/" setup.py && \  
python setup.py install  
  
RUN apk del .build-deps  
  
RUN cp conf/config_sample.py conf/config.py  
  
CMD twistd --nodaemon --python=launcher.tac  

