FROM ubuntu:trusty  
MAINTAINER tiryoh  
  
RUN apt-get update -q && \  
apt-get install -yq wget curl  
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" >
/etc/apt/sources.list.d/ros-latest.list'  
RUN curl -k https://raw.githubusercontent.com/ros/rosdistro/master/ros.key |
sudo apt-key add -  
RUN apt-get update -q && \  
apt-get install -y ros-indigo-desktop-full \  
python-rosinstall \  
ros-indigo-ros-controllers \  
ros-indigo-gazebo-ros-control && \  
rm -rf /var/lib/apt/lists/*  
RUN rosdep init  
  
RUN useradd -m -d /home/ubuntu ubuntu -p `perl -e 'print crypt("password",
"salt"),"\n"'` && \  
echo "ubuntu ALL=(ALL) ALL" >> /etc/sudoers  
  
USER ubuntu  
WORKDIR /home/ubuntu  
ENV HOME=/home/ubuntu \  
CATKIN_SHELL=bash  
RUN rosdep update  
RUN mkdir -p ~/catkin_ws/src \  
&& /bin/bash -c '. /opt/ros/indigo/setup.bash; catkin_init_workspace
$HOME/catkin_ws/src' \  
&& /bin/bash -c '. /opt/ros/indigo/setup.bash; cd $HOME/catkin_ws;
catkin_make'  
RUN echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc \  
&& echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc  
ENTRYPOINT ["bash"]  
CMD ["--login"]  

