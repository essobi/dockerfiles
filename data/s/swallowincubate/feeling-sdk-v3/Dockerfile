FROM centos:6  
RUN set -x && \  
yum groupinstall -y 'Development Tools' && \  
yum install -y readline-devel zlib-devel atlas-devel && \  
curl -s -o /etc/yum.repos.d/devtools-2.repo
https://people.centos.org/tru/devtools-2/devtools-2.repo && \  
yum --enablerepo=testing-devtools-2-centos-6 install -y devtoolset-2-gcc
devtoolset-2-gcc-c++  
  
# intall latest git  
WORKDIR /tmp/git-build  
RUN set -x && \  
yum remove -y git && \  
curl -sL https://github.com/git/git/archive/v2.17.1.tar.gz | tar zx --strip-
components 1 && \  
make configure && \  
./configure --prefix=/usr && \  
make all && \  
make install  
  
# install openssl  
ENV OPENSSL_DIR=/usr/local/ssl  
WORKDIR /tmp/openssl  
RUN set -x && \  
curl -sL https://www.openssl.org/source/openssl-1.1.0h.tar.gz | tar zx
--strip-components 1 && \  
./Configure linux-x86_64 no-shared no-dso no-hw no-engine no-async no-unit-
test -fvisibility=hidden --prefix=$OPENSSL_DIR \--openssldir=$OPENSSL_DIR && \  
make depend && \  
make -j4 && \  
make install  
  
# install ruby  
WORKDIR /tmp/ruby-build  
RUN set -x && \  
yum install -y openssl-devel && \  
curl -sL https://github.com/rbenv/ruby-build/archive/v20180424.tar.gz | tar zx
--strip-components 1 && \  
PREFIX=/usr/local ./install.sh && \  
ruby-build 2.5.1 ~/ruby && \  
echo 'export PATH="$HOME/ruby/bin:$PATH"' >> ~/.bashrc  
  
# install cmake  
WORKDIR /tmp/cmake  
RUN curl -sLo cmake.sh
https://cmake.org/files/v3.10/cmake-3.10.3-Linux-x86_64.sh && \  
sh cmake.sh --skip-license --prefix=/usr/local  
  
ARG SDK_DEPENDENCIES="lapack-devel"  
RUN set -x && \  
yum install -y $SDK_DEPENDENCIES && \  
echo "source /opt/rh/devtoolset-2/enable" >> ~/.bashrc  
RUN yum install -y https://centos6.iuscommunity.org/ius-release.rpm  
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip  
  
ARG SWIG_DEPENDENCIES="pcre-devel devtoolset-2-binutils.x86_64
devtoolset-2-binutils-devel.x86_64"  
WORKDIR /tmp/swig-build  
RUN set -x && \  
yum remove -y swig && \  
yum install -y $SWIG_DEPENDENCIES && \  
curl -sL https://github.com/swig/swig/archive/rel-3.0.12.tar.gz | tar zx
--strip-components 1 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  

