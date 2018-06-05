FROM centos:6  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:/opt/rh/devtoolset-2/root/usr/bin:$PATH  
  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6  
  
RUN yum update -y && \  
yum install -y bzip2 \  
make \  
patch \  
sudo \  
tar \  
which \  
&& yum -y clean all  
  
# Install devtoolset 2.  
RUN yum update -y && \  
yum install -y \  
centos-release-scl \  
yum-utils && \  
yum-config-manager --add-repo
http://people.centos.org/tru/devtools-2/devtools-2.repo && \  
yum update -y && \  
yum install -y \  
devtoolset-2-binutils \  
devtoolset-2-gcc \  
devtoolset-2-gcc-c++ && \  
yum clean all  
  
RUN cd /tmp \  
&& curl -sSO https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh \  
&& /bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR \  
&& conda update -y --all \  
&& conda install -y conda-build anaconda-client numpy tqdm \  
&& pip install twine \  
&& conda clean -y -a \  
&& rm -rf ~/.cache \  
&& conda config --add channels glotzer \  
&& rm Miniconda3-latest-Linux-x86_64.sh  
  
# install end point repo for git 1.8.4 needed by circleci  
RUN cd /tmp \  
&& curl -sSO https://packages.endpoint.com/rhel/6/os/x86_64/endpoint-
repo-1.6-1.x86_64.rpm \  
&& yum localinstall -y endpoint-repo-1.6-1.x86_64.rpm \  
&& yum -y clean all \  
&& rm endpoint-repo-1.6-1.x86_64.rpm  
  
RUN yum install -y git \  
&& yum -y clean all  
  
# install CUDA  
RUN curl -SL
https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-
run > /root/cuda_linux-run \  
&& bash /root/cuda_linux-run --silent --toolkit --toolkitpath=/opt/cuda \  
&& rm -f /root/cuda_linux-run  
  
RUN mkdir -p /nfs \  
&& chmod go+rx /nfs  

