# This is a sample Dockerfile you can modify to deploy your own app based on
face_recognition  
# Modified version of https://github.com/ageitgey/face_recognition by Mark
Peng  
  
FROM python:2.7-slim  
  
RUN apt-get -y update  
RUN apt-get install -y --fix-missing \  
build-essential \  
cmake \  
gfortran \  
git \  
wget \  
curl \  
graphicsmagick \  
libgraphicsmagick1-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libboost-all-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libswscale-dev \  
pkg-config \  
python-dev \  
python-numpy \  
python-setuptools \  
software-properties-common \  
zip \  
libffi-dev \  
libssl-dev \  
libopenblas-dev \  
portaudio19-dev \  
python-pyaudio \  
python-opencv \  
&& apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
# Install OpenCV  
RUN cd ~ && \  
mkdir -p ocv-tmp && \  
cd ocv-tmp && \  
curl -L https://github.com/Itseez/opencv/archive/2.4.11.zip -o ocv.zip && \  
unzip ocv.zip && \  
cd opencv-2.4.11 && \  
mkdir release && \  
cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D BUILD_PYTHON_SUPPORT=ON \  
-D ENABLE_AVX=ON \  
-D WITH_TBB=ON \  
-D WITH_V4L=ON \  
-D WITH_FFMPEG=OFF \  
.. && \  
make -j8 && \  
make install && \  
rm -rf ~/ocv-tmp  
  
# Install dlib  
RUN cd ~ && \  
mkdir -p dlib && \  
git clone -b 'v19.7' --single-branch https://github.com/davisking/dlib.git
dlib/ && \  
cd dlib/ && \  
python setup.py install --yes USE_AVX_INSTRUCTIONS  
  
  
# Install face_recognition dependencies and pre-trained models  
RUN pip install face_recognition_models \  
Click \  
dlib \  
numpy \  
Pillow \  
scipy \  
face_recognition  

