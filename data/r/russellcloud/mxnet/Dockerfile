FROM russellcloud/opencv:latest-py2  
MAINTAINER RussellCloud Team "support@russellcloud.cn"  
  
RUN git clone --recursive https://github.com/dmlc/mxnet/ && cd mxnet && \  
cp make/config.mk . && \  
echo "USE_BLAS=openblas" >>config.mk && \  
make -j$(nproc)  
  
ENV PYTHONPATH /mxnet/python

