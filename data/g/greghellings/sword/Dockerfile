FROM fedora:latest  
  
ADD . /sword-src/  
  
WORKDIR /sword-src  
  
RUN \  
dnf install -y clucene-core clucene-core-devel \  
libicu libicu-devel \  
libcurl libcurl-devel \  
cmake \  
gcc-c++ \  
make \  
python python-devel \  
perl perl-devel \  
swig \  
redhat-rpm-config \  
zlib zlib-devel \  
&& mkdir -p build \  
&& cd build \  
&& cmake \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_BUILD_TYPE=Debug \  
-DSWORD_BINDINGS="Python Perl" \  
.. \  
&& make -j10 \  
&& make install \  
&& dnf -y remove clucene-core-devel \  
libicu-devel \  
libcurl-devel \  
cmake \  
gcc-c++ \  
make \  
python-devel \  
perl-devel \  
swig \  
redhat-rpm-config \  
zlib-devel \  
&& dnf clean all  
  
CMD /bin/bash  

