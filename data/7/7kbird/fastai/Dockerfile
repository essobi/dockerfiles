FROM tensorflow/tensorflow:1.4.0-gpu-py3  
  
# Theano  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gfortran \  
git \  
liblapack-dev \  
libopenblas-dev \  
graphviz \  
cmake \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Cython for libgpuarray  
RUN pip install --no-cache-dir Cython nose  
  
# Clone libgpuarray repo and move into it  
RUN cd /root && \  
git clone https://github.com/Theano/libgpuarray.git && \  
cd libgpuarray && \  
git checkout tags/v0.7.5 -b v0.7.5 && \  
mkdir Build && cd Build && \  
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr && \  
make -j"$(nproc)" && \  
make install  
  
# Install pygpu  
RUN cd /root/libgpuarray && \  
python setup.py build_ext -L /usr/lib -I /usr/include && \  
python setup.py install && \  
cd /root && \  
rm -fr /root/libgpuarray/*  
  
# Install Theano  
RUN pip install --upgrade --no-deps --no-cache-dir
git+git://github.com/Theano/Theano.git@rel-1.0.1#egg=Theano && \  
echo
"[global]\ndevice=cuda\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN\nforce_device=True
\  
\n[lib]\ncnmem=0.1 \  
\n[nvcc]\nfastmath=True \  
\n[dnn]\nenabled=True \  
\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \  
\n[DebugMode]\ncheck_finite=1" > /root/.theanorc  
  
# Pytorch  
RUN pip install --upgrade --no-cache-dir
http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl
&& \  
pip install --no-cache-dir torchvision  
  
# Learning environments  
RUN pip install --no-cache-dir \  
keras==2.0.9 \  
mechanicalsoup \  
progressbar2 \  
bcolz \  
jupyter_contrib_nbextensions  
  
RUN jupyter contrib nbextension install --user && \  
jupyter nbextensions_configurator enable --user  
  
# inherit ENTRYPOINT and CMD from tensorflow docker  

