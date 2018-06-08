FROM ros:indigo  
  
RUN apt-get update && apt-get install -y \  
python-catkin-pkg python-rosdep python-wstool \  
python-catkin-tools ros-indigo-catkin \  
&& rm -rf /var/lib/apt/lists  
  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
RUN apt-get update && apt-get install -y \  
libeigen3-dev \  
build-essential software-properties-common \  
&& rm -rf /var/lib/apt/lists  
  
RUN apt-get update && apt-get install -y \  
ros-indigo-cv-bridge ros-indigo-image-transport \  
ros-indigo-interactive-markers ros-indigo-cmake-modules \  
libyaml-cpp-dev \  
&& rm -rf /var/lib/apt/lists  
  
RUN mkdir -p projects/tracking/src \  
&& cd projects/tracking/src \  
&& git clone https://github.com/filtering-library/fl.git \  
&& git clone https://github.com/ICRA2017/dbot.git \  
&& git clone https://github.com/ICRA2017/dbot_ros_msgs.git \  
&& git clone https://github.com/ICRA2017/dbot_ros.git  
  
RUN source /ros_entrypoint.sh \  
&& cd projects/tracking \  
&& catkin_make -DCMAKE_BUILD_TYPE=Release -DDBOT_BUILD_GPU=Off  
  
RUN cd projects/tracking/src \  
&& git clone https://git-amd.tuebingen.mpg.de/open-
source/dbot_getting_started.git  
  
RUN source /ros_entrypoint.sh \  
&& cd projects/tracking \  
&& catkin_make -DCMAKE_BUILD_TYPE=Release -DDBOT_BUILD_GPU=Off  
  
CMD ["roslaunch", "dbot_example", "launch_example_cpu.launch"]

