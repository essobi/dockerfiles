FROM opensuse:latest  
  
RUN zypper update -y && \  
zypper install -y \  
git \  
gcc-c++ \  
cmake \  
ninja \  
make \  
automake \  
autoconf \  
vim \  
which \  
curl \  
perl \  
go \  
m4 \  
libtool \  
binutils \  
net-tools \  
telnet \  
python-pyOpenSSL \  
python-pip \  
unzip  
  
RUN pip install pip --upgrade  
RUN pip install PyOpenSSL --upgrade  
RUN pip install cpp-coveralls  
  
RUN mkdir -pv /vetulus  
  
WORKDIR /vetulus  
  
ADD . /vetulus/  
  
RUN cd /vetulus/scripts/ && bash install_deps.sh  

