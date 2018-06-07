FROM keiserlabnick/cuda8.0-cudnn7-ubuntu14.04  
# Install bleeding-edge Theano and Lasagne  
RUN pip install --upgrade pip  
RUN pip install --upgrade six  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
RUN pip install --upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip  
RUN echo
"[global]\ndevice=cuda\nfloatX=float32\n[lib]\ncnmem=0.1\n[nvcc]\nfastmath=True"
> /root/.theanorc  
  

