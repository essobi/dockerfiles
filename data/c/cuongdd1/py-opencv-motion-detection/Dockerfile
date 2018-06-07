FROM i386/ubuntu:16.04  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
VOLUME /usr/local/src  
  
ENV AWS_DEFAULT_REGION= AWS_ACCESS_KEY_ID= AWS_SECRET_ACCESS_KEY=
RTSP_VIDEO_STREAM_URL=rtsp://user:pass@camera-ip.com/iphone/chanel
CAMERA_GUID=CameraID DELTA_THRESHOLD=1000  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
cmake \  
git \  
wget \  
unzip \  
pkg-config \  
libswscale-dev \  
python3-dev \  
python3-numpy \  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libavformat-dev \  
inotify-tools \  
&& apt-get -y clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  
  
RUN cv_version='3.2.0' \  
&& wget https://github.com/Itseez/opencv/archive/"$cv_version".zip \  
&& unzip "$cv_version".zip \  
&& mkdir /opencv-"$cv_version"/cmake_binary \  
&& cd /opencv-"$cv_version"/cmake_binary \  
&& cmake -D ENABLE_SSE3=OFF -D ENABLE_SSSE3=OFF -D ENABLE_SSE41=OFF -D
ENABLE_SSE42=OFF -D ENABLE_POPCNT=OFF -D ENABLE_AVX=OFF -D ENABLE_AVX2=OFF -D
ENABLE_FMA3=OFF -D CMAKE_BUILD_TYPE=DEBUG .. \  
&& make install \  
&& rm /"$cv_version".zip \  
&& rm -r /opencv-"$cv_version"  
  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python3 get-pip.py \  
&& pip install argparse datetime imutils awscli boto3 \  
&& rm get-pip.py  
  
CMD python3 /usr/local/src/movement.py --video ${RTSP_VIDEO_STREAM_URL}
\--identity=${CAMERA_GUID} \--delta-threshold=${DELTA_THRESHOLD}

