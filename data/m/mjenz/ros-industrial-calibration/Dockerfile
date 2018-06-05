FROM mjenz/ros-indigo-perception  
  
RUN apt-get update && \  
apt-get install -y \  
cmake \  
libgoogle-glog-dev \  
libatlas-base-dev \  
libeigen3-dev \  
libsuitesparse-dev \  
ros-indigo-moveit-ros \  
ros-indigo-roslint \  
ros-indigo-openni2-camera && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp/ceres  
RUN curl http://ceres-solver.org/ceres-solver-1.11.0.tar.gz -o ceres-
solver-1.11.0.tar.gz && \  
tar -xvzf ceres-solver-1.11.0.tar.gz && \  
mkdir ceres-bin && \  
cd ceres-bin && \  
cmake ../ceres-solver-1.11.0 && \  
make -j3 && \  
make install && \  
rm -rf /tmp/ceres  
  
WORKDIR /catkin_ws  
RUN mkdir src && \  
git clone https://github.com/ros-industrial/industrial_calibration.git
src/industrial_calibration && \  
. /opt/ros/indigo/setup.sh && \  
catkin_make install && \  
rm -rf build/ devel/  
  
CMD ["bash"]  
  

