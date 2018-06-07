FROM fedora:27 as builder  
  
RUN dnf install -y \  
boost-devel \  
botan-devel \  
log4cplus-devel \  
gtest-devel \  
postgresql postgresql-devel \  
gcc-c++ \  
automake libtool \  
procps-ng procps \  
iproute net-tools \  
supervisor \  
gtest-devel \  
curl  
  
# get gtest release 1.8 sources  
WORKDIR /gtest  
RUN curl -OL https://github.com/google/googletest/archive/release-1.8.0.tar.gz
&& tar xzf release-1.8.0.tar.gz  
  
# build and install kea  
WORKDIR /kea  
COPY . .  
RUN autoreconf -if  
RUN ./configure \  
\--with-dhcp-pgsql \  
\--with-gtest-source=/gtest/googletest-release-1.8.0  
RUN make -j`nproc`  
RUN make install  
  
FROM fedora:27  
RUN dnf install -y \  
boost \  
botan \  
log4cplus \  
postgresql \  
procps-ng procps \  
iproute net-tools \  
supervisor \  
gtest \  
curl  
  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/kea.conf  
RUN ldconfig  
  
COPY \--from=builder /usr/local /usr/local/  
  
# try to slim down a bit  
RUN dnf autoremove && dnf clean all  
  
CMD ["supervisord", "-n"]  

