FROM condaforge/linux-anvil  
  
# Install TeXLive, AMD APP SDK 3.0, and NVIDIA CUDA 9.1 for building OpenMM
and Omnia projects  
#  
# Install EPEL and extra packages  
#  
# CUDA requires dkms libvdpau  
# TeX installation requires wget and perl  
# The other TeX packages installed with `tlmgr install` are required for
OpenMM's sphinx docs  
# libXext libSM libXrender are required for matplotlib to work  
# Download and install EPEL, install extra packages for TeX, AMD, and CUDA,
cleanup yum  
RUN curl -L http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm \--output epel-release-6-8.noarch.rpm && \  
rpm -i \--quiet epel-release-6-8.noarch.rpm && \  
rm -rf epel-release-6-8.noarch.rpm && \  
yum install -y \--quiet perl dkms libvdpau git wget libXext libSM libXrender
groff && \  
yum clean -y \--quiet expire-cache && \  
yum clean -y \--quiet all  
  
#  
# Install TeXLive  
#  
# Add config file from repo  
ADD texlive.profile .  
# Download, untar, install, remove install files, install additional packages,
make symlinks for all users  
RUN curl -L http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
\--output install-tl-unx.tar.gz && \  
tar -xzf install-tl-unx.tar.gz && \  
cd install-tl-* && ./install-tl -profile /texlive.profile && cd \- && \  
rm -rf install-tl-unx.tar.gz install-tl-* texlive.profile && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install \  
cmap fancybox titlesec framed fancyvrb threeparttable \  
mdwtools wrapfig parskip upquote float multirow hyphenat caption \  
xstring fncychap tabulary capt-of eqparbox environ trimspaces && \  
ln -s /usr/local/texlive/2017/bin/x86_64-linux/* /usr/local/sbin/  
ENV PATH=/usr/local/texlive/2017/bin/x86_64-linux:$PATH  
  
  
#  
# Install AMD APP SDK 3.0  
#  
# Download, untar, install AMD APP SDK, remove tarball, install script, and
samples  
RUN curl -L http://s3.amazonaws.com/omnia-ci/AMD-APP-
SDKInstaller-v3.0.130.135-GA-linux64.tar.bz2 > AMD-APP-
SDKInstaller-v3.0.130.135-GA-linux64.tar.bz2 && \  
tar xjf AMD-APP-SDKInstaller-v3.0.130.135-GA-linux64.tar.bz2 && \  
./AMD-APP-SDK-v3.0.130.135-GA-linux64.sh \-- -s -a yes && \  
rm -f AMD-APP-SDK-v3.0.130.135-GA-linux64.sh AMD-APP-
SDKInstaller-v3.0.130.135-GA-linux64.tar.bz2 && \  
rm -rf /opt/AMDAPPSDK-3.0/samples/  
ENV OPENCL_HOME=/opt/AMDAPPSDK-3.0
OPENCL_LIBPATH=/opt/AMDAPPSDK-3.0/lib/x86_64  
#  
# Install CUDA 9.0  
#  
# Install minimal CUDA components (this may be more than needed)  
RUN curl -L
https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda-repo-
rhel6-9-1-local-9.1.85-1.x86_64 > cuda-repo-
rhel6-9-1-local-9.1.85-1.x86_64.rpm && \  
rpm \--quiet -i cuda-repo-rhel6-9-1-local-9.1.85-1.x86_64.rpm && \  
yum \--nogpgcheck localinstall -y \--quiet /var/cuda-repo-9-1-local/cuda-
minimal-build-9-1-9.1.85-1.x86_64.rpm && \  
yum \--nogpgcheck localinstall -y \--quiet /var/cuda-repo-9-1-local/cuda-
cufft-dev-9-1-9.1.85-1.x86_64.rpm && \  
yum \--nogpgcheck localinstall -y \--quiet /var/cuda-repo-9-1-local/cuda-
driver-dev-9-1-9.1.85-1.x86_64.rpm && \  
rpm \--quiet -i \--nodeps \--nomd5 /var/cuda-repo-9-1-local/xorg-x11-drv-
nvidia-libs-387.26-1.el6.x86_64.rpm && \  
rpm \--quiet -i \--nodeps \--nomd5 /var/cuda-repo-9-1-local/xorg-x11-drv-
nvidia-devel-387.26-1.el6.x86_64.rpm && \  
rpm \--quiet -i \--nodeps \--nomd5 /var/cuda-repo-9-1-local/cuda-
nvrtc-9-1-9.1.85-1.x86_64.rpm && \  
rpm \--quiet -i \--nodeps \--nomd5 /var/cuda-repo-9-1-local/cuda-nvrtc-
dev-9-1-9.1.85-1.x86_64.rpm && \  
rpm \--quiet -i \--nodeps \--nomd5 /var/cuda-repo-9-1-local/cuda-
runtime-9-1-9.1.85-1.x86_64.rpm && \  
yum \--nogpgcheck localinstall -y \--quiet /var/cuda-repo-9-1-local/cuda-
driver-dev-9-1-9.1.85-1.x86_64.rpm && \  
rm -rf /cuda-repo-rhel6-9-1-local-9.1.85-1.x86_64.rpm /var/cuda-
repo-9-1-local/*.rpm /var/cache/yum/cuda-9-1-local/ && \  
yum clean -y \--quiet expire-cache && \  
yum clean -y \--quiet all  

