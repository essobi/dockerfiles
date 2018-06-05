# docker build -t beast .  
FROM dorowu/ubuntu-desktop-lxde-vnc  
  
WORKDIR /tmp  
  
RUN apt-get update && apt-get install -y \  
# libx11-6 libxext-dev libxrender-dev libxtst-dev \  
ant \  
build-essential \  
autoconf \  
automake \  
libtool \  
subversion \  
pkg-config \  
git \  
openjdk-7-jdk  
  
# Clean-up  
RUN apt-get -y autoremove  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN which gcc  
RUN gcc --version  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8  
ENV ROOT_HOME /root  
ENV USER_HOME /home/ubuntu  
  
# Clone and install Beast from sources  
WORKDIR ${ROOT_HOME}  
RUN git clone \--depth=1 https://beast-dev@github.com/beast-dev/beast-mcmc.git  
WORKDIR ${ROOT_HOME}/beast-mcmc  
RUN ls  
RUN ant linux  
RUN mkdir -p /usr/local  
RUN mv ${ROOT_HOME}/beast-mcmc/release/Linux/BEASTv1* /usr/local/beast  
  
# Clone BEAGLE from source and compile without architecture optimization  
WORKDIR ${ROOT_HOME}  
RUN git clone \--depth=1 https://beagle-lib@github.com/beagle-dev/beagle-
lib.git  
WORKDIR ${ROOT_HOME}/beagle-lib  
RUN ./autogen.sh  
RUN ./configure --disable-sse --disable-march-native --prefix=/usr/local  
RUN make install  
  
# Install CUDA 7.5-runtime  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
ENV NVIDIA_GPGKEY_SUM
bd841d59a27a406e513db7d405550894188a4c1cd96bf8aa4f82f1b39e0b5c1c  
ENV NVIDIA_GPGKEY_FPR 889bee522da690103c4b085ed88c3d385c37d3be  
  
RUN apt-key adv --fetch-keys
http://developer.download.nvidia.com/compute/cuda/repos/GPGKEY && \  
apt-key adv --export \--no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +2 >
cudasign.pub && \  
echo "$NVIDIA_GPGKEY_SUM cudasign.pub" | sha256sum -c --strict - && rm
cudasign.pub && \  
echo "deb
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64 /" >
/etc/apt/sources.list.d/cuda.list  
  
ENV CUDA_VERSION 7.5  
LABEL com.nvidia.cuda.version="7.5"  
  
ENV CUDA_PKG_VERSION 7-5=7.5-18  
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-$CUDA_PKG_VERSION \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-$CUDA_VERSION /usr/local/cuda && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/cuda/lib" >> /etc/ld.so.conf.d/cuda.conf && \  
echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# Install CUDA 7.5-development  
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes \  
cuda-core-$CUDA_PKG_VERSION \  
cuda-misc-headers-$CUDA_PKG_VERSION \  
cuda-command-line-tools-$CUDA_PKG_VERSION \  
cuda-license-$CUDA_PKG_VERSION \  
cuda-nvrtc-dev-$CUDA_PKG_VERSION \  
cuda-cusolver-dev-$CUDA_PKG_VERSION \  
cuda-cublas-dev-$CUDA_PKG_VERSION \  
cuda-cufft-dev-$CUDA_PKG_VERSION \  
cuda-curand-dev-$CUDA_PKG_VERSION \  
cuda-cusparse-dev-$CUDA_PKG_VERSION \  
cuda-npp-dev-$CUDA_PKG_VERSION \  
cuda-cudart-dev-$CUDA_PKG_VERSION \  
cuda-driver-dev-$CUDA_PKG_VERSION && \  
cd /tmp && apt-get download gpu-deployment-kit && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /tmp/gpu-deployment-kit && cd /tmp/gpu-deployment-kit && \  
dpkg -x /tmp/gpu-deployment-kit_*.deb . && \  
mv usr/include/nvidia/gdk/* /usr/local/cuda/include && \  
mv usr/src/gdk/nvml/lib/* /usr/local/cuda/lib64/stubs && \  
rm -rf /tmp/gpu-deployment-kit*  
  
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs:${LIBRARY_PATH}  
  
# Create standard user  
RUN useradd --create-home --shell /bin/bash --user-group --groups adm,sudo
ubuntu  
RUN echo "ubuntu:ubuntu" | chpasswd  
RUN echo 'export PS1="[beast docker \u] \W # "' >> ${USER_HOME}/.bashrc  
RUN echo 'export
PATH=/usr/local/beast/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:$PATH' >>
${USER_HOME}/.bashrc  
RUN echo 'export
LD_LIBRARY_PATH=/usr/local/lib:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}'
>> ${USER_HOME}/.bashrc  
RUN echo 'export LIBRARY_PATH=/usr/local/cuda/lib64/stubs:${LIBRARY_PATH}' >>
${USER_HOME}/.bashrc  
RUN sudo -u ubuntu -i bash -c "mkdir -p /home/ubuntu/.config/pcmanfm/LXDE/ \  
&& cp /usr/share/doro-lxde-wallpapers/desktop-items-0.conf
/home/ubuntu/.config/pcmanfm/LXDE/"  
  
# Run VNC  
EXPOSE 6080  
WORKDIR /root  
  
ADD startup.sh /  
ADD run_server.sh /  
ADD reinstall_beagle /usr/local/bin  
  
ENTRYPOINT ["/startup.sh"]  
  
#ENTRYPOINT ["su", "-l", "ubuntu"]

