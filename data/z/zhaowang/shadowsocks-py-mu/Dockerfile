FROM ubuntu:14.04  
MAINTAINER soapril <soapril@outlook.com>  
  
RUN apt-get update && apt-get -y install language-pack-en  
RUN apt-get -y install build-essential python python-dev python-pip git
python-m2crypto  
RUN pip install cymysql  
RUN git clone -b manyuser https://github.com/fsgmhoward/shadowsocks-py-mu.git
manyuser  
RUN apt-get install -y supervisor  
RUN apt-get clean && \  
rm -rf /var/lib/apt/list/*  
COPY supervisor.conf /etc/supervisor/conf.d/  
COPY config.py /manyusers/shadowsocks/  
WORKDIR /manyusers/shadowsocks/  
  
CMD ['/usr/bin/supervisord']  

