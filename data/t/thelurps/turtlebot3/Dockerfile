FROM ros:kinetic-robot-xenial  
  
MAINTAINER Joshua Schraven  
  
RUN apt-get update && apt-get install --assume-yes \  
vim-nox \  
sudo \  
python-pip \  
ros-kinetic-desktop-full \  
ros-kinetic-turtlebot3 \  
ros-kinetic-turtlebot3-bringup \  
ros-kinetic-turtlebot3-description \  
ros-kinetic-turtlebot3-fake \  
ros-kinetic-turtlebot3-gazebo \  
ros-kinetic-turtlebot3-msgs \  
ros-kinetic-turtlebot3-navigation \  
ros-kinetic-turtlebot3-simulations \  
ros-kinetic-turtlebot3-slam \  
ros-kinetic-turtlebot3-teleop  
  
# install python packages  
RUN pip install -U scikit-learn numpy scipy  
RUN pip install --upgrade pip  
  
# create non-root user  
ENV USERNAME ros  
RUN adduser --ingroup sudo --disabled-password --gecos "" \--shell /bin/bash
--home /home/$USERNAME $USERNAME  
RUN bash -c 'echo $USERNAME:ros | chpasswd'  
ENV HOME /home/$USERNAME  
USER $USERNAME  
  
# create catkin_ws  
RUN mkdir /home/$USERNAME/catkin_ws  
WORKDIR /home/$USERNAME/catkin_ws  
  
# add catkin env  
RUN echo 'source /opt/ros/kinetic/setup.bash' >> /home/$USERNAME/.bashrc  
RUN echo 'source /home/$USERNAME/catkin_ws/devel/setup.bash' >>
/home/$USERNAME/.bashrc  

