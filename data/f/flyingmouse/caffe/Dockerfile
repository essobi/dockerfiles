# Start with Caffe dependencies  
FROM flyingmouse/caffe-deps  
MAINTAINER Haoming Wang <haoming.exe@gmail.com>  
  
ENV CAFFE_ROOT=/root/caffe  
WORKDIR $CAFFE_ROOT  
  
ADD Makefile.config $CAFFE_ROOT/Makefile.config  
RUN make all && make test && make runtest && make pycaffe  
  
# Add to Python path  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  

