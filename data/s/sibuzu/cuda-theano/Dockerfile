FROM sibuzu/cuda-caffe  
  
ARG THEANO_VERSION=rel-0.8.2  
  
# Install Theano and set up Theano config (.theanorc) for CUDA and OpenBLAS  
RUN pip --no-cache-dir install
git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \  
pip install nose-parameterized && \  
pip install pycuda && \  
\  
echo
"[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN
\  
\n[lib]\ncnmem=0.95 \  
\n[nvcc]\nfastmath=True \  
\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \  
\n[DebugMode]\ncheck_finite=1" \  
> /root/.theanorc  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

