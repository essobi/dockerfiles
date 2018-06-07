FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y software-properties-common python build-essential wget
cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-
dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-
dev libjasper-dev libdc1394-22-dev imagemagick  
WORKDIR /opt  
RUN wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-
unix/2.4.11/opencv-2.4.11.zip  
RUN apt-get install -y unzip libqt4-dev  
RUN unzip opencv-2.4.11.zip  
WORKDIR /opt/opencv-2.4.11  
RUN mkdir /opt/opencv-2.4.11/release  
WORKDIR /opt/opencv-2.4.11/release  
RUN cmake -G "Unix Makefiles" -D CMAKE_CXX_COMPILER=/usr/bin/g++
CMAKE_C_COMPILER=/usr/bin/gcc -D CMAKE_BUILD_TYPE=RELEASE -D
CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON
-D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D
BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D BUILD_FAT_JAVA_LIB=ON -D
INSTALL_TO_MANGLED_PATHS=ON -D INSTALL_CREATE_DISTRIB=ON -D INSTALL_TESTS=ON
-D ENABLE_FAST_MATH=ON -D WITH_IMAGEIO=ON -D BUILD_SHARED_LIBS=OFF -D
WITH_GSTREAMER=ON -D WITH_FFMPEG=OFF ..  
RUN make all -j8 # 8 cores  
RUN make install  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
RUN mkdir -p /opt  
RUN echo "fresh clone please yo"  
RUN git clone https://github.com/neufeldtech/face-detection-nodejs.git
/opt/face-detection-nodejs  
WORKDIR /opt/face-detection-nodejs  
RUN mkdir /opt/yolo  
RUN npm install  
EXPOSE 8008  
ENV NODE_PORT 8008  
CMD ["/usr/bin/node", "/opt/face-detection-nodejs/index.js"]  

