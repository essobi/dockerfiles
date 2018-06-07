FROM nimbix/centos-base:6  
MAINTAINER stephen.fox@nimbix.net  
  
ENV TOOLCHAIN=/opt/rh/devtoolset-3/enable  
ENV SLURM_VERSION=16.05.4  
ENV INSTALL_ROOT=/opt  
ENV BUILD_DIR=/usr/local/src  
ENV MUNGE_VER=0.5.11  
RUN yum install -y centos-release-scl && yum install -y devtoolset-3-gcc-
gfortran devtoolset-3-toolchain devtoolset-4-toolchain devtoolset-4-gcc-
gfortran rpm-build bzip2-devel openssl-devel zlib-devel  
  
# Install Munge  
WORKDIR /usr/local/src  
RUN curl -L -o munge-${MUNGE_VER}.zip
https://github.com/dun/munge/archive/munge-${MUNGE_VER}.zip  
RUN unzip munge-${MUNGE_VER}.zip && mv munge-munge-${MUNGE_VER}
munge-${MUNGE_VER} && tar cjf munge-${MUNGE_VER}.tar.bz2 munge-${MUNGE_VER} &&
rm munge-${MUNGE_VER}.zip && rm -rf munge-${MUNGE_VER}  
RUN source ${TOOLCHAIN} && rpmbuild -tb --clean munge-${MUNGE_VER}.tar.bz2  
WORKDIR /root/rpmbuild/RPMS/x86_64  
RUN rpm -ivh *.rpm  
  
# Build Slurm and install to /opt  
WORKDIR /usr/local/src  
RUN curl -L -o slurm-${SLURM_VERSION}.tar.bz2
http://www.schedmd.com/download/latest/slurm-${SLURM_VERSION}.tar.bz2 && tar
xjf slurm-${SLURM_VERSION}.tar.bz2 && rm *.tar.bz2  
RUN yum install -y readline-devel perl pam-devel  
  
WORKDIR /usr/local/src/slurm-16.05.4  
RUN source ${TOOLCHAIN} && ./configure
--prefix=${INSTALL_ROOT}/slurm-${SLURM_VERSION} && make -j4 && make install  
RUN rm -rf ${BUILD_DIR} && rm -rf /root/rpmbuild  
  
ADD ./conf /opt/conf  
RUN ln -sf /opt/slurm-${SLURM_VERSION} /opt/slurm  
ADD ./scripts/startslurm.sh /opt/slurm/startslurm.sh  

