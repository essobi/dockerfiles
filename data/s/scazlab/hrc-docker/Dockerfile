FROM ros:indigo-robot  
FROM ros:indigo-perception  
  
SHELL ["/bin/bash", "-c"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set up work directory  
RUN useradd ros  
RUN mkdir /home/ros && chown -R ros: /home/ros  
ENV HOME "/home/ros"  
# This is useful when adding python stuff in user space  
ENV PATH="/home/ros/.local/bin:${PATH}"  
# This suppresses some python SSL warnings  
ENV PYTHONWARNINGS="ignore:a true SSLContext object"  
WORKDIR /home/ros  
  
# Add manually Eigen3 and g++-4.9  
RUN apt-get update && apt-get -y install software-properties-common
libeigen3-dev  
RUN apt-get -y install gfortran libopenblas-dev liblapack-dev  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN apt-get update && apt-get -y install gcc-4.9 g++-4.9  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 50  
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 50  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
# RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
RUN apt-get -y install git-core python-argparse python-wstool python-vcstools
python-rosdep python-pip \  
ros-indigo-control-msgs ros-indigo-joystick-drivers python-catkin-tools  
  
RUN pip2 install numpy scipy scikit-learn  
  
# Upgrade pip to fix this https://github.com/ros-
infrastructure/rosdep/issues/420  
RUN pip2 install pip --upgrade  
  
USER ros  
RUN rosdep update  
RUN mkdir -p ~/ros_ws/src && cd ~/ros_ws/src \  
&& wstool init . \  
&& wstool merge
https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
\  
&& wstool update  
USER root  
RUN cd ~/ros_ws \  
&& rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO  
USER ros  
RUN cd ~/ros_ws && catkin init  
RUN cd ~/ros_ws && source /opt/ros/$ROS_DISTRO/setup.bash && catkin build  
USER root  
  
# ENV ROS_MASTER_URI="http://baxter.local:11311"  
COPY ./ros-entrypoint.sh /bin/  
RUN ["chmod", "+x", "/bin/ros-entrypoint.sh"]  
ENTRYPOINT ["/bin/ros-entrypoint.sh"]  
  
RUN chown -R ros: /home/ros  
USER ros  
CMD ["/bin/bash"]  

