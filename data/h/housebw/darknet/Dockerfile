FROM alantrrs/cuda-opencv:latest  
  
ADD . /darknet  
RUN cd /darknet && \  
make LIBSO=1 GPU=1 CUDNN=1 OPENCV=1 OPENMP=1 -j 8

