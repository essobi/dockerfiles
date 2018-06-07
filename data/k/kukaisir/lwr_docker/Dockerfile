FROM ros:indigo-ros-base  
MAINTAINER Jimmy Da Silva jimmy.dasilva@isir.upmc.fr  
  
# Install additionnal useful packages  
RUN apt-get update && apt-get install -y -qq \  
bash-completion \  
build-essential \  
git \  
module-init-tools \  
nautilus \  
python-rosinstall \  
software-properties-common \  
tmux \  
vim \  
wget  
  
# Install and configure Nvidia  
RUN apt-get install -y -qq binutils mesa-utils  
RUN add-apt-repository ppa:xorg-edgers/ppa && apt-get update  
RUN apt-get install -y -qq nvidia-352 nvidia-settings  
RUN ldconfig  
ENV QT_X11_NO_MITSHM 1  
# Now create the ros user itself  
RUN adduser --gecos "ROS User" \--disabled-password ros  
RUN usermod -a -G dialout ros  
ADD 99_aptget /etc/sudoers.d/99_aptget  
RUN chmod 0440 /etc/sudoers.d/99_aptget && chown root:root
/etc/sudoers.d/99_aptget  
  
# Choose to run as user  
ENV USER ros  
USER ros  
  
# Change HOME environment variable  
ENV HOME /home/ros  
  
# Installation script  
RUN sudo wget https://raw.githubusercontent.com/kuka-
isir/lwr_setup/master/lwr_setup.bash  
RUN sudo mv lwr_setup.bash /sbin/lwr_install  
RUN sudo chmod +x /sbin/lwr_install ; sudo chown ros /sbin/lwr_install ; sync
; sudo -H -u ros bash -c /sbin/lwr_install ; sudo rm /sbin/lwr_install  
  
# Change .bashrc  
COPY update_bashrc /sbin/update_bashrc  
RUN sudo chmod +x /sbin/update_bashrc ; sudo chown ros /sbin/update_bashrc ;
sync ; /bin/bash -c /sbin/update_bashrc ; sudo rm /sbin/update_bashrc  
  
# Change entrypoint to source ~/.bashrc and start in ~  
COPY entrypoint.sh /ros_entrypoint.sh  
RUN sudo chmod +x /ros_entrypoint.sh ; sudo chown ros /ros_entrypoint.sh ;  
  
# Clean image  
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/ros_entrypoint.sh"]  
CMD ["bash"]  

