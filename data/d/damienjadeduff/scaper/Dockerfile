# This is a comment  
FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y build-essential git mercurial libboost-all-dev
libspnav-dev libqt4-dev libflann-dev libvtk5-dev libvtk5-qt4-dev
libusb-1.0-0-dev libusb-1.0-0-dev libeigen3-dev cmake-curses-gui libopenni-dev
libopenni-sensor-primesense0 libopenni-sensor-primesense-dev libopenni0
openni-utils libeigen3-dev libopenni2-dev openni2-utils alsoft-conf libopenal-
dev libalut-dev libalut0 libopenal1 openni2-utils libqt4-opengl libqtcore4
libqtgui4 sox libsox-dev stk libstk0-dev stk-doc dos2unix wget  
RUN mkdir -p /home/sensory/software  
RUN mkdir /tmp ; cd /tmp && wget
http://files.djduff.net/Download/DepthSense/DepthSenseSDK-1.9.0-5-amd64-deb.run
&& chmod u+x DepthSenseSDK-1.9.0-5-amd64-deb.run  
RUN cd /tmp && ./DepthSenseSDK-1.9.0-5-amd64-deb.run \--accept-eula  
RUN cd /home/sensory/software && git clone
https://github.com/damienjadeduff/pcl.git  
RUN cd /home/sensory/software/pcl && mkdir build  
RUN cd /home/sensory/software/pcl/build && cmake -DCMAKE_BUILD_TYPE=Release
-DBUILD_apps=ON -DBUILD_segmentation=ON -DWITH_DSSDK=ON -DBUILD_features=on
-DBUILD_io=ON -DBUILD_stereo=ON -DBUILD_recognition=ON -DPCL_QT_VERSION=4
-DBUILD_filters=ON -DBUILD_search=ON -DBUILD_kdtree=ON -DWITH_OPENNI=ON
-DWITH_OPENNI2=ON -DWITH_QT=ON -DWITH_VTK=ON -DWITH_ENSENSO=OFF
-DWITH_DAVIDSDK=OFF ..  
RUN cd /home/sensory/software/pcl/build && make pcl_common pcl_kdtree
pcl_octree pcl_search pcl_io pcl_filters pcl_features pcl_keypoints pcl_ml  
# RUN cd /home/sensory/software/pcl/build && make -j 3  
# RUN cd /home/sensory/software && git clone
https://bitbucket.org/damienjadeduff/scaper.git && mkdir scaper/build  
# RUN cd /home/sensory/software/scaper/build && cmake
-DPCL_DIR=/home/sensory/software/pcl/build -DCMAKE_BUILD_TYPE=Debug .. && make  
MAINTAINER Damien Jade Duff <djduff@itu.edu.tr>

