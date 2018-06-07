FROM ros:kinetic  
MAINTAINER Alexander Krupenkin <mail@akru.me>  
LABEL Description="DroneEmployee developer image" Vendor="DroneEmployee"
Version="0.2"  
  
EXPOSE 14550/udp  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Install deps  
RUN apt-get update \  
&& apt-get install -y sudo liblas-dev liblas-c-dev liblas-bin python-
sqlalchemy python-psycopg2  
RUN echo "%users ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN useradd -m -g users ros  
  
USER ros  
  
# Prepare  
RUN mkdir -p ~/workspace/src && cd ~/workspace/src \  
&& git clone \--recursive https://github.com/DroneEmployee/drone_employee_ros
\  
&& . /opt/ros/kinetic/setup.sh \  
&& catkin_init_workspace \  
&& cd .. \  
&& rosdep update \  
&& rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y  
  
# Build the FCL  
RUN sudo apt-get install -y libccd-dev liboctomap-dev \  
&& cd ~ \  
&& git clone https://github.com/flexible-collision-library/fcl.git -b fcl-0.3
\  
&& cd fcl && patch -p1 <
~/workspace/src/drone_employee_ros/small_atc/data/octomap_found.patch \  
&& mkdir build \  
&& cd build \  
&& cmake .. && make -j2 \  
&& sudo make install \  
&& cd ~ && rm -rf fcl  
  
# Build DroneEmployee  
RUN cd ~/workspace \  
&& . /opt/ros/kinetic/setup.sh \  
&& catkin_make -j1  

