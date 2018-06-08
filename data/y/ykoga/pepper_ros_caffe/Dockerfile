FROM ykoga/caffe_cpu  
  
RUN apt-get update && apt-get -y upgrade && apt-get install -y ros-indigo-
naoqi-pose ros-indigo-naoqi-driver  
RUN apt-get install -y ros-indigo-pepper-robot ros-indigo-pepper-bringup ros-
indigo-pepper-description  
RUN apt-get install -y ros-indigo-keyboard  
RUN apt-get install -y tmux nano emacs  
  
WORKDIR /root  
  
RUN mkdir naoqi-sdk/  
RUN mkdir pynaoqi/  
  
ENV PYTHONPATH $PYTHONPATH:/root/pynaoqi/  
  
RUN echo "source /opt/ros/indigo/setup.bash" >> /root/.bashrc  
RUN /bin/bash -c 'source /root/.bashrc'  
  
# clone ros_caffe project by ruffsl  
RUN mkdir -p catkin_ws/src \  
&& cd catkin_ws/src \  
&& git clone https://github.com/ruffsl/ros_caffe.git \  
&& git clone https://github.com/ykoga-kyutech/pepper_ros_handson.git  
  
# modify CMakeLists for building ros_caffe package by CPU only  
RUN cd catkin_ws/src/ros_caffe && \  
sed -i '/#add_definitions(-DCPU_ONLY=1)/s/^#//' CMakeLists.txt && \  
sed -i '/find_package(CUDA REQUIRED)/s/^/#/' CMakeLists.txt && \  
sed -i '/${CUDA_INCLUDEDIR}/s/^/#/' CMakeLists.txt && \  
sed -i '/^ *cuda/s/^/#/' CMakeLists.txt  
  
# add launches for running ros_caffe only and ros_caffe + webcam + viewer  
ADD ros_caffe.launch /root/catkin_ws/src/ros_caffe/launch/ros_caffe.launch  
ADD ros_caffe_webcam_uvc.launch
/root/catkin_ws/src/ros_caffe/launch/ros_caffe_webcam_uvc.launch  
ADD test_webcam.bag /root/catkin_ws/src/  
  
# build ros_caffe package  
RUN cd catkin_ws/src/ros_caffe/ && \  
wget https://raw.githubusercontent.com/ruffsl/ros_caffe/master/docker/ros-
caffe/build.sh && \  
chmod a+x build.sh && \  
./build.sh  
RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc  
RUN /bin/bash -c 'source /root/.bashrc'  
  
# get model  
RUN cd /root/catkin_ws/src/ros_caffe && \  
python get_model.py  

