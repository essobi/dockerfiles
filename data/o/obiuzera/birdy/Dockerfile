FROM tensorflow/tensorflow:1.4.1-gpu-py3  
  
RUN apt-get update && apt-get install -y \  
python-opencv \  
libopenblas-dev \  
python-qt4 \  
libopencv-dev \  
python3-tk \  
git \  
build-essential \  
cmake && \  
update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3 &&
\  
apt-get clean && apt-get autoremove  
  
RUN pip install Cython  
RUN pip install Mako  
RUN pip install numpy scipy==0.19.1 scikit-learn==0.19.1  
RUN pip install matplotlib==2.1.0  
RUN pip install keras==2.0.6  
RUN pip install librosa  
RUN pip install --upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip  
RUN pip install --upgrade
https://github.com/dnouri/nolearn/archive/master.zip#egg=nolearn  
RUN pip install pandas==0.20.3  
RUN pip install munkres==1.0.7  
RUN pip install opencv-python  
RUN pip install python_speech_features  
RUN pip install xmltodict  
RUN pip install Augmentor  
RUN pip install h5py  
  
RUN pip install pudb  
  
RUN git clone https://github.com/Theano/libgpuarray.git && \  
mkdir -p libgpuarray/Build && \  
cd libgpuarray/Build && \  
cmake .. -DCMAKE_BUILD_TYPE=Release && \  
make && \  
make install && \  
cd .. && \  
ldconfig && \  
python3 setup.py build && \  
python3 setup.py install && \  
cd .. && rm -rf libgpuarray  
  
RUN pip install --upgrade
https://github.com/Theano/Theano/archive/master.zip#egg=Theano  
  
RUN apt-get update && apt-get dist-upgrade -y && apt-get clean && apt-get
autoremove  

