FROM terminus7/gpu-py2  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
ARG THEANO_VERSION=rel-0.9.0  
  
# new system dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y --no-install-recommends \  
g++ \  
libblas-dev \  
python-tk \  
cmake \  
git && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
# Theano  
RUN pip install --no-deps --no-cache-dir
git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \  
\  
echo
"[global]\ndevice=cuda\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN
\  
\n[lib]\ncnmem=0.95\n \  
\n[nvcc]\nfastmath=True\n \  
\n[DebugMode]\ncheck_finite=1" \  
> /root/.theanorc  
  
# libgpuarray python dependencies  
RUN pip install --no-cache-dir \  
numpy \  
Cython  
  
  
# libgpuarray + pygpu  
RUN git clone https://github.com/Theano/libgpuarray.git && \  
cd libgpuarray && \  
mkdir Build && \  
cd Build && \  
cmake .. \  
-DCMAKE_BUILD_TYPE=Release && \  
make && \  
make install && \  
cd .. && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rf libgpuarray  
  
RUN ldconfig  
  
# python dependencies  
# TODO: using git until scikit-cuda@0.5.2 is realeased  
RUN pip --no-cache-dir install \  
matplotlib \  
pandas \  
pillow \  
scikit-image \  
scipy \  
git+https://github.com/lebedov/scikit-cuda.git#egg=scikit-cuda  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

