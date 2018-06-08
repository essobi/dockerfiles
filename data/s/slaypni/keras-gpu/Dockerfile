FROM tensorflow/tensorflow:0.10.0-devel-gpu  
  
ENV KERAS_BACKEND tensorflow  
  
RUN apt-get update && apt-get install -y \  
libpython3-dev \  
libhdf5-dev \  
graphviz  
  
RUN pip2 install numpy && pip2 install scipy && pip2 install \  
pyyaml \  
h5py \  
keras \  
pydot==1.1.0 \  
graphviz  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.4  
  
RUN pip3 install numpy && pip3 install scipy && pip3 install \  
pyyaml \  
h5py \  
keras \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp34-cp34m-linux_x86_64.whl
\  
pydot-ng \  
graphviz  

