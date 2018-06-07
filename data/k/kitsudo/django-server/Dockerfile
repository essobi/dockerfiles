FROM kitsudo/aliyun_centos6.6  
MAINTAINER Dave Luo <kitsudo163@163.com>  
RUN yum install -y \  
curl \  
wget \  
tar \  
gcc \  
mysql-server \  
libjpeg-turbo-devel \  
python-devel \  
zlib-devel \  
mysql-devel \  
sqlite-devel \  
openssl \  
openssl-devel \  
memcached \  
&& \  
echo "[Prepare]"  
  
RUN cd /tmp && \  
wget http://mirrors.sohu.com/python/2.7.12/Python-2.7.12.tgz && \  
tar xfz Python-2.7.12.tgz && \  
cd Python-2.7.12 && \  
./configure --prefix=/usr/local && \  
make && \  
make altinstall && \  
echo "[Python]"  
# RUN curl -LS "https://bootstrap.pypa.io/get-pip.py" | python2.7 && \  
# echo "[pip]"  
RUN cd /tmp && \  
wget
http://mirrors.aliyun.com/pypi/packages/6b/dd/a7de8caeeffab76bacf56972b3f090c12e0ae6932245abbce706690a6436/setuptools-28.3.0.tar.gz
&& \  
tar -zxvf setuptools-28.3.0.tar.gz && \  
cd setuptools-28.3.0 && \  
python2.7 setup.py install && \  
wget
http://mirrors.aliyun.com/pypi/packages/e7/a8/7556133689add8d1a54c0b14aeff0acb03c64707ce100ecd53934da1aa13/pip-8.1.2.tar.gz
&& \  
tar -xzvf pip-8.1.2.tar.gz && \  
cd pip-8.1.2 && \  
python2.7 setup.py install && \  
echo "[pip]"  
  
# 默认的一些基本库  
RUN pip2.7 install Django MySQL-python requests python-memcached supervisor
--trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple  
EXPOSE 8000  
WORKDIR /app/server  
ENTRYPOINT ["/app/server/centos_start.sh"]  
CMD [""]  

