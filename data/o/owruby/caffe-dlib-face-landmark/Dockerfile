FROM tleyden5iwx/caffe-cpu-master  
  
MAINTAINER ruby.yano1995@gmail.com  
  
WORKDIR /home/gender_estimation  
  
ADD ./ /home/gender_estimation/dlib-gender  
  
RUN apt-get update  
  
# Download dlib  
RUN wget --no-check-certificate
https://github.com/davisking/dlib/archive/master.tar.gz && \  
tar xpvf master.tar.gz && \  
rm master.tar.gz  
  
# Build dlib  
RUN cd ./dlib-master && \  
cp -f /home/gender_estimation/dlib-gender/CMakeLists.txt ./ && \  
cp /home/gender_estimation/dlib-gender/face_landmark_detection_ex.cpp ./ && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make all && \  
mkdir result_faces  
  
# Download dat file  
RUN cd ./dlib-master/build && \  
apt-get install -y bzip2 && \  
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && \  
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2  
  
# NOT ERROR  
RUN ln /dev/null /dev/raw1394

