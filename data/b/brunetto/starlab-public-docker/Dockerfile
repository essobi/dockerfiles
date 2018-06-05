FROM ubuntu:14.04  
  
MAINTAINER brunetto ziosi <brunetto.ziosi@gmail.com>  
  
# Public version of StarLab4.4.4, see http://www.sns.ias.edu/~starlab/  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV STARLAB_DOWNLOAD
https://www.dropbox.com/s/tzwimr7e9hrmpm1/starlabDockerPublic.tar.gz  
ENV STARLAB_FILE starlabDockerPublic.tar.gz  
  
# This has to be set by hand and MUST be the same of the host  
##############  
# longisland #  
##############  
# ENV CUDA_DRIVER 340.46  
# ENV CUDA_INSTALL
http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-
Linux-x86_64-${CUDA_DRIVER}.run  
# ENV CUDA_TOOLKIT cuda_6.0.37_linux_64.run  
# ENV CUDA_TOOLKIT_DOWNLOAD
http://developer.download.nvidia.com/compute/cuda/6_0/rel/installers/$CUDA_TOOLKIT  
##############  
# uno #  
##############  
# ENV CUDA_DRIVER 331.38  
# ENV CUDA_INSTALL
http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-
Linux-x86_64-${CUDA_DRIVER}.run  
# ENV CUDA_TOOLKIT cuda_5.5.22_linux_64.run  
# ENV CUDA_TOOLKIT_DOWNLOAD
http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/$CUDA_TOOLKIT  
##############  
# spritz #  
##############  
ENV CUDA_DRIVER 331.113  
ENV CUDA_INSTALL
http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-
Linux-x86_64-${CUDA_DRIVER}.run  
ENV CUDA_TOOLKIT cuda_5.5.22_linux_64.run  
ENV CUDA_TOOLKIT_DOWNLOAD
http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/$CUDA_TOOLKIT  
################  
# sfursat #  
# to be tested #  
################  
# ENV CUDA_DRIVER 270.41.19  
# ENV CUDA_INSTALL
http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-
Linux-x86_64-${CUDA_DRIVER}.run  
# ENV CUDA_TOOLKIT ????  
# ENV CUDA_TOOLKIT_DOWNLOAD ????????  
  
# Update and install minimal.  
RUN apt-get update --quiet && apt-get install --yes \  
\--no-install-recommends --no-install-suggests \  
build-essential module-init-tools wget libboost-all-dev  
  
# Clean up packages.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install CUDA.  
RUN wget $CUDA_INSTALL -P /tmp --no-verbose \  
&& chmod +x /tmp/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run \  
&& /tmp/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run -s -N --no-kernel-module \  
&& rm -rf /tmp/*  
  
RUN wget $CUDA_TOOLKIT_DOWNLOAD && chmod +x $CUDA_TOOLKIT  
RUN ./$CUDA_TOOLKIT -toolkit -toolkitpath=/usr/local/cuda-site -silent
-override  
RUN rm $CUDA_TOOLKIT  
RUN echo "PATH=$PATH:/usr/local/cuda-site/bin" >> .bashrc  
RUN echo "LD_LIBRARY_PATH=/usr/local/cuda-site/lib64" >> .bashrc  
RUN . /.bashrc  
RUN ldconfig /usr/local/cuda-site/lib64  
  
# Install StarLab  
# Sapporo  
RUN wget --no-check-certificate $STARLAB_DOWNLOAD  
RUN tar -xvf $STARLAB_FILE && rm $STARLAB_FILE  
RUN cp -r starlab starlab-no-GPU  
RUN mv starlab starlab-GPU  
RUN cd sapporo/ && make && bash compile.sh && cd ../  
  
# With GPU  
RUN cd /starlab-GPU/ && ./configure --with-f77=no && make && make install &&
cd ../  
RUN mv /starlab-GPU/usr/bin slbin && rm -rf /starlab-GPU  
  
# Without GPU  
RUN cd /starlab-no-GPU/ && ./configure --with-f77=no --with-grape=no \  
&& make && make install && cd ../  
RUN mv /starlab-no-GPU/usr/bin slbin-no-GPU && rm -rf /starlab-no-GPU  
  
# Default command.  
ENTRYPOINT ["/bin/bash"]  
  

