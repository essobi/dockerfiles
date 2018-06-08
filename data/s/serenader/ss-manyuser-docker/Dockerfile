FROM centos  
MAINTAINER serenader xyslive@gmail.com  
  
RUN yum -y update && yum install -y python-setuptools git python-devel libffi-
devel openssl-devel && yum -y groupinstall "Development Tools" && yum clean
all  
  
RUN easy_install pip  
  
RUN curl -O -L
https://github.com/jedisct1/libsodium/releases/download/1.0.16/libsodium-1.0.16.tar.gz  
  
RUN tar xf libsodium-1.0.16.tar.gz && cd libsodium-1.0.16 && ./configure &&
make -j2 && make install  
  
RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf && ldconfig  
  
WORKDIR /shadowsocks  
  
RUN git clone -b manyuser https://github.com/esdeathlove/shadowsocks.git && cd
shadowsocks && pip install -r requirements.txt && cp config.json user-
config.json  
  
CMD ["python", "/shadowsocks/shadowsocks/server.py"]  

