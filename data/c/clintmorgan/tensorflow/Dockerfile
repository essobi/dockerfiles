FROM python:3.5  
RUN mkdir /work  
WORKDIR /work  
  
RUN export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp35-cp35m-linux_x86_64.whl
&& \  
pip3 install --upgrade $TF_BINARY_URL

