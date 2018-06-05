FROM ubuntu:14.04.1  
MAINTAINER OSHIMA YUJI <yuji.oshima0x3fd@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends python python-setuptools
python-pip unzip wget git gcc python-dev  
  
ENV HOME /root  
WORKDIR /root  
  
RUN git config --global http.sslVerify false  
RUN git clone https://github.com/Orange-OpenSource/bagpipe-bgp.git  
RUN cd bagpipe-bgp && python setup.py install  
RUN mkdir /var/log/bagpipe-bgp  
RUN touch /var/log/bagpipe-bgp/bagpipe-bgp.log  
RUN cd bagpipe-bgp && ./install_bagpipe_bgp.sh  

