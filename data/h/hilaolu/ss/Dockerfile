FROM centos:latest  
MAINTAINER Captain Dao <support@daocloud.io>  
EXPOSE 8443  
RUN yum update -y \  
&& yum install -y python \  
python-pip \  
python-setuptools \  
wget \  
unzip \  
gcc \  
python-devel \  
libffi-devel \  
openssl-devel  
RUN easy_install pip  
RUN yum -y groupinstall "Development Tools"  
RUN yum clean all  
RUN mkdir /var/ss  
RUN mkdir /var/libsodium  
WORKDIR /var/ss/libsodium  
RUN wget
https://github.com/jedisct1/libsodium/releases/download/1.0.11/libsodium-1.0.11.tar.gz
&& tar xf libsodium-1.0.11.tar.gz  
WORKDIR libsodium-1.0.11  
RUN ./configure && make -j2 && make install  
RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf  
RUN ldconfig  
RUN rm /var/ss/libsodium/libsodium-1.0.11.tar.gz  
RUN wget --no-check-certificate
https://github.com/hilaolu/shadowsocks/archive/manyuser.zip -O
/tmp/manyuser.zip && unzip -d /tmp /tmp/manyuser.zip && mv /tmp/shadowsocks-
manyuser /var/ss/shadowsocks && rm -rf /tmp/*  
WORKDIR /var/ss/shadowsocks  
RUN pip install -r requirements.txt  
ENTRYPOINT python /var/ss/shadowsocks/server.py  
  

