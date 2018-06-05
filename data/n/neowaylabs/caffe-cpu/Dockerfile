FROM neowaylabs/caffe-cpu:1.0.0  
ENV PYTHONPATH /opt/caffe/python  
  
# Add caffe binaries to path  
ENV PATH $PATH:/opt/caffe/.build_release/tools  
  
# Using a fork of Caffe containing some important modifications.  
RUN cd /opt/caffe && \  
git remote add fork https://github.com/neowaylabs/caffe.git && \  
git fetch fork && \  
git checkout -f multilabel && \  
make pycaffe  

