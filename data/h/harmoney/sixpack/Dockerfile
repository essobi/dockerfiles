FROM ubuntu:14.04  
MAINTAINER Naoki AINOYA <ainonic@gmail.com>  
MAINTAINER Nik Rolls <nik.rolls@harmoney.co.nz>  
  
# setup Python, build tools and environment  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y python-setuptools python-dev git build-essential  
RUN apt-get install -y libyaml-dev  
# PyYAML version must be kept up to date with requirement in  
# https://github.com/seatgeek/sixpack/blob/master/requirements.txt  
RUN easy_install pip pyyaml==3.10  
RUN echo 'root:sixpack' | chpasswd  
  
# setup supervisord  
RUN pip install supervisor  
RUN mkdir -p /etc/supervisord.d/  
RUN mkdir -p /var/log/supervisor  
ADD template/supervisord.conf /etc/supervisord.conf  
ADD template/supervisord.d/sixpack-web.ini /etc/supervisord.d/sixpack-web.ini  
ADD template/supervisord.d/sixpack.ini /etc/supervisord.d/sixpack.ini  
  
# setup sixpack  
RUN mkdir -p /home/sixpack  
WORKDIR /home/sixpack  
RUN git clone https://github.com/harmoney-dev/sixpack  
WORKDIR /home/sixpack/sixpack  
RUN pip install -r requirements.txt  
  
# start server  
# 5000 & 5001: sixpack, 24224: td-agent  
EXPOSE 5000 5001 24224  
WORKDIR /home/sixpack  
CMD supervisord -c /etc/supervisord.conf  

