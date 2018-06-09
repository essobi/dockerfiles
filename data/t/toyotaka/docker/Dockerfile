FROM toyotaka/tensorflow:v0.2  
  
MAINTAINER toyotaka <toyotaka.tanaka@growup-system.co.jp>  
  
#OPENCV2 INSTALL  
RUN apt-get update && apt-get install -y \  
build-essential \  
python-numpy \  
cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \  
python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev
libjasper-dev \  
# libdc1394-22-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /root \  
&& \  
git clone https://github.com/Itseez/opencv.git  
  
RUN mkdir /root/opencv/release \  
&& \  
cd /root/opencv/release \  
&& \  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
WITH_CUDA=ON CUDA_nvcuvid_LIBRARY=/usr/local/cuda ..  
  
RUN cd /root/opencv/release \  
&& \  
make \  
&& \  
make install  
  
RUN ldconfig  
  
RUN apt-get update && apt-get install -y \  
python-numpy cmake zlib1g-dev libjpeg-dev libboost-all-dev gcc libsdl2-dev
wget unzip \  
autoconf automake libtool libpcre3-dev bison g++ \  
liblapack-dev libatlas-base-dev gfortran g++ \  
&& \  
git clone https://github.com/swig/swig.git && \  
cd swig/ && \  
./autogen.sh && ./configure && make && make install swig \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
\--upgrade tqdm gym[all]  
  
RUN git clone https://github.com/devsisters/DQN-tensorflow.git  
  
#RUN ln /usr/lib/x86_64-linux-gnu/libcudnn.so.4 /usr/lib/x86_64-linux-
gnu/libcudnn.so  
# TensorBoard  
EXPOSE 6006  
# IPython  
#EXPOSE 8888  
  
RUN ["/bin/bash"]  

