FROM osrf/ros:lunar-desktop-full-xenial  
#FROM ct2034/vnc-ros-kinetic-full  
  
#Set the working directory to /files  
WORKDIR /root/files  
  
#Add files  
ADD . /root/files  
  
RUN apt-get update && apt-get install -y \  
git-core \  
nano \  
python-argparse \  
python-wstool \  
python-vcstools \  
python-rosdep \  
python-rosinstall \  
ros-lunar-geographic-msgs \  
ros-lunar-control-msgs \  
ros-lunar-joystick-drivers \  
python3 \  
python \  
wget  
  
#RUN rosdep init && rosdep update  
  
RUN apt-get install -y python3-pip python-pip && \  
pip3 install --trusted-host pypi.python.org -r requirements.txt && \  
pip install --trusted-host pypi.python.org -r requirements_2.txt  
  
RUN . /opt/ros/lunar/setup.sh && \  
mkdir -p ros_ws/src && \  
cd ros_ws && \  
catkin_make && \  
catkin_make install  
  
RUN cd ros_ws/src && \  
wstool init . && \  
wstool merge
https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
&& \  
wstool update  
  
RUN . /opt/ros/lunar/setup.sh && \  
cd ros_ws && \  
catkin_make && \  
catkin_make install  
  
RUN apt install -y libsm6 \  
libxext6 \  
libgtk2.0-dev && \  
pip3 install opencv-python && \  
pip install opencv-python  
  
RUN cd ros_ws && \  
wget https://github.com/RethinkRobotics/baxter/raw/master/baxter.sh && \  
chmod u+x baxter.sh  
  
RUN git clone https://github.com/KenYF/Files_GENG5508.git && \  
rm Dockerfile \  
requirements.txt \  
requirements_2.txt \  
cloudbuild.yaml \  
README.md  
  
EXPOSE 80 11311  
  
#CMD ["jupyter","lab","--allow-root","--ip=0.0.0.0"]  
#CMD ["bash"]  

