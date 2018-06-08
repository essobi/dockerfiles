FROM drigerg/computer-vision  
  
MAINTAINER Pradeep Kumar A.V. <pradeepkumar1025@gmail.com>  
  
RUN pip install pydot_ng nnpack h5py scikit-learn && \  
python -c 'import h5py;h5py.run_tests()'  
  
# TensorFlow  
RUN git clone \--depth 1 https://github.com/tensorflow/tensorflow.git
/usr/src/tensorflow && \  
pip install -q tensorflow  
RUN pip install tflearn  
  
RUN mkdir -p /tmp/tensorflow  
  
ENTRYPOINT ["tensorboard", "--log", "/tmp/tensorflow"]  

