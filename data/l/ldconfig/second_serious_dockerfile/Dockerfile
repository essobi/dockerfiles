FROM centos:6.6  
# Need this patch to overcome "Rpmdb checksum is invalid: dCDPT(pkg
checksums)" bug  
RUN yum install -y yum-plugin-ovl  
RUN yum -y update  
RUN yum -y install ntp  
  
# Basic packages  
RUN yum -y install wget which sudo openssh-clients openssh-server  
  
# Epel needed for lmdb  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
RUN rpm -ivh epel-release-latest-6.noarch.rpm  
  
# Devtoolset-2 to get gcc-4.8  
RUN wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O
/etc/yum.repos.d/devtools-2.repo  
RUN yum -y install devtoolset-2-gcc devtoolset-2-gcc-c++ devtoolset-2-binutils  
  
# Development tools  
RUN yum -y groupinstall 'Development Tools' && yum clean all  
  
# Openmpi and headers  
RUN yum -y install openmpi-devel cmake redhat-lsb-core  
  
RUN yum -y install \  
libXi-devel libXmu-devel libXrandr-devel \  
libXinerama-devel libXcursor-devel mesa-libGLU-devel mesa-libGL-devel libX11  
  
RUN yum clean all  
  
RUN useradd -ms /bin/bash builder  
RUN mkdir -p /home/builder/.ssh  
RUN chmod 700 /home/builder/.ssh  
RUN mkdir -p /home/builder/rpmbuild/RPMS  
RUN mkdir -p /home/builder/rpmbuild/RPMS/BUILD  
RUN mkdir -p /home/builder/rpmbuild/RPMS/BUILDROOT  
RUN mkdir -p /home/builder/rpmbuild/RPMS/RPMS  
RUN mkdir -p /home/builder/rpmbuild/RPMS/SOURCES  
RUN mkdir -p /home/builder/rpmbuild/RPMS/SPECS  
RUN mkdir -p /home/builder/rpmbuild/RPMS/SRPMS  
RUN chown -R builder:builder /home/builder  
  
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib" >
/home/builder/.bashrc  
RUN echo "export PATH=$PATH:/usr/lib64/openmpi/bin" >> /home/builder/.bashrc  
  
RUN usermod -aG wheel builder  
RUN sed -i 's/^#[ \t]*%wheel[ \t]*ALL=(ALL)[ \t]*NOPASSWD:[ \t]*ALL/%wheel
ALL=(ALL) NOPASSWD: ALL/' /etc/sudoers  
  
USER builder  
WORKDIR /home/builder

