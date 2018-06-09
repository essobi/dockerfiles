FROM mstormo/suse:11SP3  
  
LABEL Description="SUSE with various CUDA versions for quick build of producs
based on customer configuration"  
MAINTAINER Marius Storm-Olsen <mstormo@gmail.com>  
  
# Use /data as the persistant storage for seismic  
VOLUME ["/data"]  
  
# 11.3  
RUN zypper ar http://demeter.uni-regensburg.de/SLE11SP3-SDK-x64/DVD1/ SLE-DVD1
\  
&& zypper ar http://demeter.uni-regensburg.de/SLE11SP3-SDK-x64/DVD2/ SLE-DVD2  
  
#
--------------------------------------------------------------------------------------------------  
# Layer: Development tools  
#  
# We do all the installations of development tools in a single layer, to
optimize the layer size, as each  
# layer can only add size, not remove (so uninstalling packages and package
manager cleanup is later layers  
# does not make the final image smaller).  
#
--------------------------------------------------------------------------------------------------  
RUN \  
# SuSE 11.* repos seem to be VERY unstable (few mirrors), so update repos upto
3 times, just to be sure  
zypper --gpg-auto-import-keys --non-interactive ref -fdb \  
|| zypper --gpg-auto-import-keys --non-interactive ref -fdb \  
|| zypper --gpg-auto-import-keys --non-interactive ref -fdb; \  
# - install development basis package and Qt 4 sdk
-------------------------------------------------  
zypper --non-interactive install --no-recommends --download-in-advance --type
pattern \  
Basis-Devel \  
sdk_qt4 \  
# - install libs and tools needed for our product development and compiling
git --------------------  
&& zypper --non-interactive install --no-recommends --download-in-advance \  
awk \  
branding-SLES \  
bzip2 \  
ccache \  
curl \  
findutils-locate \  
fontconfig-devel \  
freeglut-devel \  
freetype2-devel \  
gcc47 \  
gcc47-c++ \  
gcc47-fortran \  
gettext-runtime \  
gettext-tools \  
glibc-locale \  
gzip \  
java-1_6_0-ibm-devel \  
libcurl4 \  
libcurl-devel \  
libexpat1 \  
libexpat-devel \  
libopenssl0_9_8 \  
libopenssl-devel \  
libpng-devel \  
lsb \  
make \  
Mesa-devel \  
MesaGLw-devel \  
tar \  
zlib-devel \  
# - make gcc and g++ point to 4.7
------------------------------------------------------------------  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.7 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-4.7 \  
# - install GIT, recent version
--------------------------------------------------------------------  
&& curl -k -o /root/git-v2.5.1.tar.gz
https://codeload.github.com/git/git/tar.gz/v2.5.1 \  
&& cd /root && tar zxf /root/git-v2.5.1.tar.gz \  
&& make prefix=/usr/local -C /root/git-2.5.1 install \  
&& rm -rf /root/git-2.5.1* /root/git-v2.5.1.tar.gz \  
# - install cmake, recent version
------------------------------------------------------------------  
&& curl -o /root/cmake-2.8.12.2-Linux-i386.tar.gz
http://www.cmake.org/files/v2.8/cmake-2.8.12.2-Linux-i386.tar.gz \  
&& tar zxf /root/cmake-2.8.12.2-Linux-i386.tar.gz -C /root \  
&& cp -R /root/cmake-2.8.12.2-Linux-i386/* /usr/local/ \  
&& rm -rf /root/cmake-2.8.12.2-Linux-i386* \  
# - remove packages not needed anymore
-------------------------------------------------------------  
&& zypper --non-interactive remove \  
libcurl-devel \  
libexpat-devel \  
# - cleanup package manager
------------------------------------------------------------------------  
&& zypper --non-interactive clean --all \  
# - remove all documentation and anything in /tmp
--------------------------------------------------  
&& rm -f `find /usr/share/doc/packages -type f |grep -iv
"copying\|license\|copyright"` \  
&& rm -rf /usr/share/info \  
&& rm -rf /usr/share/man \  
&& rm -rf /tmp/*  
  
#
--------------------------------------------------------------------------------------------------  
# Layer: CUDA  
# This layer will only contain a given version of CUDA  
#
--------------------------------------------------------------------------------------------------  
# CUDA 4.2 - Uses its own install implementation, due to different packaging  
#ENV cudaPkg cudatoolkit_4.2.9_linux_64_rhel5.5.run  
#ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/4_2/rel/toolkit/$cudaPkg  
#ENV cudaLoc /usr/local/cuda  
#RUN curl -o /root/$cudaPkg $cudaUrl \  
# && chmod 755 /root/$cudaPkg \  
# && /root/$cudaPkg -- --prefix=/usr/local auto \  
# && rm -rf /root/$cudaPkg $cudaLoc/doc $cudaLoc/libnvvp $cudaLoc/bin/nvvp  
# CUDA 5.0  
#ENV cudaPkg cuda_5.0.35_linux_64_rhel5.x-1.run  
#ENV cudaUrl http://developer.download.nvidia.com/compute/cuda/5_0/rel-
update-1/installers/$cudaPkg  
#ENV cudaLoc /usr/local/cuda-5.0  
# CUDA 5.5  
#ENV cudaPkg cuda_5.5.22_linux_64.run  
#ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/$cudaPkg  
#ENV cudaLoc /usr/local/cuda-5.5  
# CUDA 6.0  
#ENV cudaPkg cuda_6.0.37_linux_64.run  
#ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/6_0/rel/installers/$cudaPkg  
#ENV cudaLoc /usr/local/cuda-6.0  
# CUDA 6.5  
#ENV cudaPkg cuda_6.5.14_linux_64.run  
#ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/$cudaPkg  
#ENV cudaLoc /usr/local/cuda-6.5  
# CUDA 7.0  
#ENV cudaPkg cuda_7.0.28_linux.run  
#ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/$cudaPkg  
#ENV cudaLoc /usr/local/cuda-7.0  
# CUDA 7.5  
ENV cudaPkg cuda_7.5.18_linux.run  
ENV cudaUrl
http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/$cudaPkg  
ENV cudaLoc /usr/local/cuda-7.5  
  
# Install CUDA, general implementation for all but 4.2  
# Also remove doc,samples,nvvp to save some space  
RUN curl -o /root/$cudaPkg $cudaUrl \  
&& chmod 755 /root/$cudaPkg \  
&& /root/$cudaPkg --silent --toolkit --override \  
# - add CUDA to ld.so.conf so linker will find it
--------------------------------------------------  
&& echo $cudaLoc/lib64 >> /etc/ld.so.conf \  
&& echo $cudaLoc/lib >> /etc/ld.so.conf \  
&& ldconfig \  
# - clean up after installation of CUDA
------------------------------------------------------------  
&& rm -rf /root/$cudaPkg \  
&& rm -rf $cudaLoc/doc $cudaLoc/jre $cudaLoc/libnsight $cudaLoc/libnvvp
$cudaLoc/bin/nvvp $cudaLoc/samples \  
&& rm -rf /tmp/*  
  
#
--------------------------------------------------------------------------------------------------  
# Next Layers:  
# Add some convenience prompts to easily see which version of SuSE and CUDA
we're using.  
# Also add an entrypoint, which ensures commands happen with user permissions,
provided the proper  
# parameters are used to invoke the image  
# docker run -e UID=$UID -v /path/to/me/code:/data <image> /bin/bash  
# if not, root permissions are used.  
#
--------------------------------------------------------------------------------------------------  
COPY root.bashrc /root/root.bashrc  
COPY user.bashrc /root/user.bashrc  
COPY entrypoint.sh /root/entrypoint.sh  
ENTRYPOINT ["/root/entrypoint.sh"]  

