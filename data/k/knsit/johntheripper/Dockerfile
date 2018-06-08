FROM nvidia/cuda:8.0-runtime as build  
  
RUN apt-get update && \  
apt-get install -y locales  
  
# Locale settings  
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen; locale-gen  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/librexgen/  
  
RUN apt-get install -y build-essential \  
yasm \  
git \  
libpcap0.8 libpcap-dev \  
pkg-config \  
libbz2-1.0 libbz2-dev \  
libssl1.0.0 libssl-dev \  
libgmp10 libgmp-dev \  
libkrb5-3 libkrb5-dev \  
libnss3 libnss3-dev \  
libopenmpi1.10 libopenmpi-dev openmpi-bin \  
cmake \  
bison \  
flex \  
libicu55 libicu-dev  
  
RUN apt-get install -y ocl-icd-libopencl1 \  
nvidia-opencl-dev && \  
mkdir -p /etc/OpenCL/vendors && \  
echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd  
  
RUN mkdir -p ~/src && \  
cd ~/src && \  
git clone \--recursive https://github.com/teeshop/rexgen.git && \  
cd rexgen && \  
sed -i -e 's/sudo//g' install.sh && \  
./build.sh && \  
./install.sh && \  
ldconfig && \  
cd ~/src && \  
git clone git://github.com/magnumripper/JohnTheRipper -b bleeding-jumbo john
&& \  
cd john/src && \  
./configure \--prefix=/usr \--enable-pkg-config \--enable-pcap \--enable-mpi
&& \  
make -s clean && \  
make -sj8  
  
FROM nvidia/cuda:8.0-runtime  
  
RUN apt-get update && \  
apt-get install -y locales  
  
COPY \--from=build /root/src/rexgen/build/librexgen /usr/local/lib/  
COPY \--from=build /root/src/rexgen/build/rexgen/rexgen /usr/bin/  
COPY \--from=build /root/src/john/run /usr/share/john  
COPY \--from=build /root/src/john/src/opencl/* /usr/share/v/kernels/  
# Locale settings  
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen; locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/librexgen/:/usr/local/nvidia/lib:/usr/local/nvidia/lib64  
ENV JOHN=/etc/john  
  
ADD john.conf /etc/john/  
ADD john.local.conf /etc/john/  
  
RUN apt-get install -y libpcap0.8 \  
libbz2-1.0 \  
libssl1.0.0 \  
libgmp10 \  
libkrb5-3 \  
libnss3 \  
libopenmpi1.10 openmpi-bin \  
bison \  
flex \  
libicu55 \  
ocl-icd-libopencl1 && \  
mkdir -p /etc/OpenCL/vendors && \  
echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \  
adduser \--home /home/john \--disabled-password \--gecos "" john && \  
cp /usr/share/john/john.bash_completion /etc/bash_completion.d/ && \  
apt-get clean  
  
RUN mv /usr/share/john/john /usr/bin/ && \  
ln -s john /usr/bin/calc_stat && \  
ln -s john /usr/bin/cprepair && \  
ln -s john /usr/bin/genmkvpwd && \  
ln -s john /usr/bin/mkvcalcproba && \  
ln -s john /usr/bin/raw2dyna && \  
ln -s john /usr/bin/relbench && \  
ln -s john /usr/bin/tgtsnarf && \  
ln -s john /usr/bin/uaf2john && \  
ln -s john /usr/bin/wpapcap2john && \  
ln -s john /usr/bin/vncpcap2john && \  
ln -s john /usr/bin/SIPdump && \  
mkdir /usr/lib/john && \  
mv /usr/share/john/*.py /usr/lib/john/ && \  
mv /usr/share/john/*.pl /usr/lib/john/ && \  
mv /usr/share/john/*.rb /usr/lib/john/ && \  
mv /usr/share/john/mailer /usr/lib/john/ && \  
mv /usr/share/john/benchmark-unify /usr/lib/john/ && \  
rm -rf /var/cache/apt/* && \  
rm -f /usr/share/john/john.conf /usr/share/john/john.local.conf  
  
USER john  
  
WORKDIR /home/john  
  
ENTRYPOINT ["/bin/bash"]  

