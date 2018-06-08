# NOTE The manylinux1 policy mandates CentOS-5. We replace it with CentOS-6 in  
# order to satisfy the build of capnproto library (a nupic.core dependency),  
# which requires some headers and symbols not present on CentOS-5 (e.g.,  
# signalfd.h, pipe2, O_NONBLOCK, SOCK_NONBLOCK, etc.). See  
# https://github.com/sandstorm-io/capnproto/issues/350.  
FROM centos:6.8  
MAINTAINER Numenta, based on the ManyLinux project  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV PATH /opt/rh/devtoolset-2/root/usr/bin:$PATH  
ENV LD_LIBRARY_PATH
/opt/rh/devtoolset-2/root/usr/lib64:/opt/rh/devtoolset-2/root/usr/lib:/usr/local/lib64:/usr/local/lib  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
  
COPY build_scripts /build_scripts  
RUN bash build_scripts/build.sh && rm -r build_scripts  
  
ENV SSL_CERT_FILE=/opt/_internal/certs.pem  

