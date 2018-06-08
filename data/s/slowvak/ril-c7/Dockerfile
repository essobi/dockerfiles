FROM centos  
  
MAINTAINER Brad Erickson <bje001@GMAIL.COM>  
  
#################################################################################################################  
# This builds a basic compute environment with GPU and parallel python #  
#################################################################################################################  
# Ensure the CUDA libs and binaries are in the correct environment variables  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-7.0/lib64  
ENV PATH=$PATH:/usr/local/cuda-7.0/bin  
CMD ["/bin/bash"]  
  
#################################################################################################################  
# basic development tools #  
#################################################################################################################  
RUN yum -y update  
RUN yum -y install git python-devel && \  
yum -y install gcc-gfortran libmpc-devel && \  
yum -y install wget && \  
yum -y install gcc-c++ && \  
yum -y install Cython  
  
RUN yum -y install epel-release  
RUN yum -y install python-pip  
RUN pip install --upgrade pip  
RUN pip install mako  
RUN yum -q -y groupinstall 'Development Tools'  
RUN yum -y install module-init-tools  
  
  
#################################################################################################################  
# CUDA stuff--if you don't want GPU support, you can delete this #  
#################################################################################################################  
# Ensure the CUDA libs and binaries are in the correct environment variables  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-7.0/lib64  
ENV PATH=$PATH:/usr/local/cuda-7.0/bin  
  
RUN cd /opt && \  
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/352.21/NVIDIA-
Linux-x86_64-352.21.run && \  
wget
http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run
&& \  
chmod +x *.run && \  
./NVIDIA-Linux-x86_64-352.21.run -s -N --no-kernel-module && \  
mkdir /opt/nvidia_installers && \  
/opt/cuda_7.0.28_linux.run -extract=/opt/nvidia_installers && \  
cd /opt/nvidia_installers && \  
chmod +x *.run && \  
./cuda-linux64-rel-*.run -noprompt  
  
# now copy the cudaNN files over--no install script available....  
ADD cudaNN/include/cudnn.h /usr/local/cuda/include/  
ADD cudaNN/lib64/* /usr/local/cuda/lib64/  
#################################################################################################################  
# OpenBLAS-Numpy stuff. If you don't want, you can delete this #  
#################################################################################################################  
# openblas can use multiple CPUs but numpy must be recompiled to use these...  
# can do this, but it will not be optimized for machine...  
#RUN yum -y install libopenblas-devel liblapack-devel  
# this is probably better...  
RUN mkdir ~/src && cd ~/src && \  
git clone https://github.com/xianyi/OpenBLAS && \  
cd ~/src/OpenBLAS && \  
make FC=gfortran && \  
make PREFIX=/opt/OpenBLAS install  
  
# now update the library system:  
RUN echo /opt/OpenBLAS/lib > /etc/ld.so.conf.d/openblas.conf  
RUN ldconfig  
ENV LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH  
  
# now install numpy source  
# this does dev version, not stable and chainer uninstalls it...  
# RUN cd ~/src && \  
# git clone https://github.com/numpy/numpy  
  
ADD numpy.tar.gz /root/src  
  
RUN echo [default] > ~/src/numpy/site.cfg && \  
echo include_dirs = /opt/OpenBLAS/include >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg && \  
echo [openblas] >> ~/src/numpy/site.cfg && \  
echo openblas_libs = openblas >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg && \  
echo [lapack] >> ~/src/numpy/site.cfg && \  
echo lapack_libs = openblas >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg  
  
  
RUN cd ~/src/numpy && \  
python setup.py config && \  
python setup.py build --fcompiler=gnu95 && \  
python setup.py install  
  
RUN pip install pycuda  
  
# add stuff to run codebox  
  
WORKDIR /workspace  
  
RUN yum install -y nodejs npm && \  
npm -g install node-gyp codebox && \  
cd /usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js && \  
make clean && make  
  
# port for codebox  
EXPOSE 8000  
# ENTRYPOINT ["/usr/bin/codebox", "run"]  
  
ENV OPENBLAS_NUM_THREADS=6  
# ADD pybench.py ~  
# RUN time python pybench.py  

