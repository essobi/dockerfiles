FROM centos:centos5  
  
MAINTAINER Omar Laurino <olaurino@cfa.harvard.edu>  
  
  
#****************************************************************************  
# Copy conda.rc and update yum configuration  
#****************************************************************************  
COPY condarc /root/.condarc  
RUN sed -i 's/enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf  
RUN sed -i 's/mirrorlist/#mirrorlist/' /etc/yum.repos.d/*.repo  
RUN sed -i
's|#baseurl=http://mirror.centos.org/centos/$releasever|baseurl=http://vault.centos.org/5.11|'
/etc/yum.repos.d/*.repo  
  
#****************************************************************************  
# Install Miniconda3 (inspired by kyoba/miniconda3-alpine)  
#****************************************************************************  
ENV PATH=/opt/conda/bin:/opt/rh/devtoolset-2/root/usr/bin:$PATH \  
MINICONDA=Miniconda3-3.19.0-Linux-x86_64.sh  
  
RUN yum update -y -qq && yum install -y -qq bzip2 make flex bison glibc-devel
wget && \  
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O
/etc/yum.repos.d/devtools-2.repo && \  
yum install -y -qq devtoolset-2-gcc devtoolset-2-binutils devtoolset-2-gcc-c++
devtoolset-2-gcc-gfortran git && \  
rpm -Uvh
ftp://ftp.pbone.net/mirror/pkgs.repoforge.org/flex/flex-2.5.35-0.8.el5.rfb.x86_64.rpm
&& \  
yum clean all && \  
wget -q --no-check-certificate https://repo.continuum.io/miniconda/$MINICONDA
&& \  
/bin/bash $MINICONDA -b -p /opt/conda && \  
rm -rf /root/.continuum /opt/conda/pkgs/* && \  
rm $MINICONDA  
  
#****************************************************************************  
# Install required conda libraries  
#****************************************************************************  
RUN conda install -y -q python=3.6.0 conda-build && \  
conda config --add channels sherpa && \  
conda config --add channels cxc/channel/dev && \  
conda clean -tipsy && \  
rm -rf /opt/conda/pkgs/*  
  
ENV MINICONDA=/opt/conda  
  
VOLUME /opt/project  
  
ENTRYPOINT ["conda", "build", "--output-folder=/opt/project/output"]  
  
CMD ["/opt/project/recipes/sherpa.conda"]  
  

