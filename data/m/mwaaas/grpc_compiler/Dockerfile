FROM amazonlinux  
  
ENV PYTHON_VERSION 3.6.1  
RUN yum -y update && \  
yum -y install \  
gcc \  
gcc-c++ \  
zip \  
make \  
zlib-devel \  
bzip2-devel \  
openssl-devel \  
readline-devel \  
ncurses-devel \  
sqlite-devel && \  
curl --remote-name --progress
https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
&& \  
echo "2d0fc9f3a5940707590e07f03ecb08b9 Python-${PYTHON_VERSION}.tgz" | md5sum
-c - && \  
tar zxf Python-${PYTHON_VERSION}.tgz && \  
cd Python-${PYTHON_VERSION} && \  
./configure --prefix=/usr/local \--enable-shared && \  
make && \  
make altinstall && \  
echo '/usr/local/lib' > /etc/ld.so.conf.d/local-libs.conf && \  
ldconfig && \  
cd .. && \  
rm -rf Python-${PYTHON_VERSION}.tgz Python-${PYTHON_VERSION}  
  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
  
RUN mkdir /usr/src/build  
COPY . /usr/src/build  
  
CMD /usr/src/build/build_lambda.sh

