FROM centos:centos6.6  
MAINTAINER Eliezio Oliveira "eliezio.oliveira@gmail.com"  
ENV RPM_GPG_DIR /etc/pki/rpm-gpg  
ADD http://puias.princeton.edu/data/puias/6/x86_64/os/RPM-GPG-KEY-puias
${RPM_GPG_DIR}/  
RUN rpm --import ${RPM_GPG_DIR}/RPM-GPG-KEY-puias  
COPY puias-*.repo /etc/yum.repos.d/  
  
# yum-plugin-ovl is required to make Yum compatible with Docker OverlayFS  
RUN yum install -y yum-plugin-ovl epel-release \  
&& yum -y install redhat-lsb-core rpm-build git cmake popt-devel zlib-devel
glib2-devel libsodium-devel \  
devtoolset-2-binutils devtoolset-2-gcc devtoolset-2-gcc-c++ \  
&& yum clean all  
  
# Fixes missing PkgConfig metadata file from popt-devel package  
COPY popt.pc /usr/lib64/pkgconfig/  
  
# Installs the Google Test Framework  
ENV GTEST_VERSION 1.8.0  
ADD https://github.com/google/googletest/archive/release-${GTEST_VERSION}.zip
/usr/local/src/  
RUN cd /usr/local/src && unzip -q release-${GTEST_VERSION}.zip && rm
release-${GTEST_VERSION}.zip  
ENV GTEST_ROOT /usr/local/src/googletest-release-${GTEST_VERSION}  
  
# Enables DevToolset-2  
ENV PATH /opt/rh/devtoolset-2/root/usr/bin:$PATH  
ENV MANPATH /opt/rh/devtoolset-2/root/usr/share/man  
ENV INFOPATH /opt/rh/devtoolset-2/root/usr/share/info  
ENV PCP_DIR /opt/rh/devtoolset-2/root  
ENV LD_LIBRARY_PATH
/opt/rh/devtoolset-2/root/usr/lib64:/opt/rh/devtoolset-2/root/usr/lib  
  
# Uses TINI to properly reap zombie processes (provided that the container's
entrypoint is not overridden)  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
RUN mkdir /build && chown nobody:nobody /build  
VOLUME /build  
  
COPY bashrc /.bashrc  
USER nobody  
  
WORKDIR /build  

