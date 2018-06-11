FROM yidian7/opencv:latest  
LABEL dlib Yin jiao<yinjiao@jcble.com>  
  
WORKDIR /usr/local/src  
  
#install dlib  
RUN apt-get -y install wget  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends python libboost-dev cmake  
RUN cd /usr/local/src &&\  
git clone \--depth 1 https://github.com/davisking/dlib.git && \  
git clone \--depth 1 https://github.com/yidian7/some_file.git && \  
mv some_file/interpolation_abstract.h dlib/dlib/image_transforms/ && \  
cd dlib/examples && \  
mkdir build && \  
cd build && \  
cmake .. && \  
cmake --build . --config Release && \  
cd ../ && \  
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && \  
bunzip2 shape_predictor_68_face_landmarks.dat.bz2  

