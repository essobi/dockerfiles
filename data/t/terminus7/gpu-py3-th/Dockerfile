FROM terminus7/gpu-py3  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
ARG THEANO_VERSION=rel-0.9.0  
  
# new system dependencies  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
g++ \  
libblas-dev \  
python-tk \  
git && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# new python dependencies  
RUN pip --no-cache-dir install \  
matplotlib \  
numpy \  
pandas \  
pillow \  
scikit-image \  
scipy \  
nose  
  
# Theano  
RUN pip install --no-deps
git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \  
\  
echo
"[global]\ndevice=cuda\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN
\  
\n[lib]\ncnmem=0.95\n \  
\n[nvcc]\nfastmath=True\n \  
\n[DebugMode]\ncheck_finite=1" \  
> /root/.theanorc  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

