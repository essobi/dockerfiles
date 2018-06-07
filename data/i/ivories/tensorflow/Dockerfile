FROM nvidia/cuda:8.0-cudnn5-devel  
  
RUN apt-get update && apt-get install -y \  
python3.5 curl && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/python3.5 /usr/bin/python  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp35-cp35m-linux_x86_64.whl  
  
RUN pip \--no-cache-dir install -U nltk tqdm  

