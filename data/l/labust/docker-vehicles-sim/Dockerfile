## Currently we use ROS-Indigo as the base  
FROM ros:indigo-ros-base  
  
## Setup the development environment  
RUN apt-get update && apt-get install -y gcc g++ make cmake ssh tmux sudo vim
bash-completion  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN pass=$(perl -e 'print crypt($ARGV[0], "password")' labos123) ;\  
useradd -p $pass -G root,adm,dialout,video,tty,sudo -s /bin/bash -m stdops  
# Enable passwordless sudo  
RUN sed -i -e 's/%sudo.ALL=(ALL:ALL) ALL/%sudo ALL=(ALL) NOPASSWD: ALL/g'
/etc/sudoers  
  
## Configure SSH globaly  
RUN ssh-keyscan bitbucket.org >> /etc/ssh/ssh_known_hosts ;\  
ssh-keyscan github.com >> /etc/ssh/ssh_known_hosts ;\  
ssh-keyscan gitlab.com >> /etc/ssh/ssh_known_hosts  
  
## Switch to stdops user operation  
USER stdops  
WORKDIR /home/stdops  
# Add private key  
RUN mkdir -p .ssh  
COPY config/labust_id_rsa .ssh/id_rsa  
RUN sudo chown stdops:stdops .ssh/id_rsa ;\  
chmod 0600 .ssh/id_rsa  
# Add source setup  
RUN echo "source /opt/ros/indigo/setup.bash" >> .bashrc  
  
## Download the ROS sources for LABUST code  
RUN mkdir -p ros/src/  
# Add rosinstall file with permission  
COPY config/rosinstall ros/src/.rosinstall  
RUN sudo chown stdops:stdops ros/src/.rosinstall  
RUN cd ros/src ;\  
wstool update  
  
# Install dependencies  
RUN rosdep update  
RUN rosdep install -y --from-paths ros/src --ignore-src --rosdistro indigo  
RUN ros/src/labust-visualization-pkg/scripts/precompile_setup.sh  
RUN ros/src/labust-ros-pkg/labust_mission/scripts/install_tinyxml2.sh  
  
## Compile LABUST repos  
RUN source /opt/ros/indigo/setup.bash ;\  
cd ros/src ;\  
catkin_init_workspace ;\  
cd ~/ros ;\  
catkin_make  
  
## Finalize configurations  
# Add devel setup  
RUN echo "source ${HOME}/ros/devel/setup.bash" >> .bashrc  
RUN echo "source ${HOME}/ros/src/vehicles-ros-pkg/scripts/ros/ros_log_dir.sh"
>> .bashrc  
# Copy hosts file  
RUN sudo cp ros/src/vehicles-ros-pkg/common_config/etc/hosts /etc/hosts  
# Configure locale  
RUN sudo locale-gen hr_HR.UTF-8  
# Add authorized ssh hosts  
COPY config/dnad_id_rsa.pub .  
RUN cat dnad_id_rsa.pub >> .ssh/authorized_keys  
RUN rm dnad_id_rsa.pub  
# Setup the permanent storage mount point  
RUN sudo mkdir /export  
RUN sudo chown stdops:stdops /export  
  
# Update the entrypoint  
COPY config/ros_entrypoint.sh /ros_entrypoint.sh  

