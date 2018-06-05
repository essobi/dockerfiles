FROM osrf/ros:kinetic-desktop-full  
  
# Utilities  
RUN apt-get -y update && apt-get install -y \  
screen \  
sudo \  
x11-apps \  
python-pip \  
build-essential \  
zsh \  
vim \  
nano \  
git  
RUN pip install catkin_tools  
  
# Fix 'Gtk-Message: Failed to load module canberra-gtk-module'  
RUN apt-get -y install libcanberra-gtk-module  
  
# Intel GPU  
RUN apt-get -y install libgl1-mesa-glx libgl1-mesa-dri mesa-utils  
  
# Nvidia GPU  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# Set the locale to utf8  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN echo "LANG=C.UTF-8\n\  
LC_ALL=C.UTF-8" > /etc/default/locale  
  
# Set SSH_CLIENT flag to force oh-my-zsh agnoster theme to show the full
user@host prompt  
RUN echo "export SSH_CLIENT=1" >> /etc/zsh/zshenv  
  
# Source ros env  
RUN echo "source /opt/ros/kinetic/setup.zsh" >> /etc/zsh/zshenv  
RUN echo "source /opt/ros/kinetic/setup.bash" >> /etc/bash.bashrc  
  
# Fix BadDrawable in rviz  
RUN echo "export QT_X11_NO_MITSHM=1" >> /etc/zsh/zshenv  
RUN echo "export QT_X11_NO_MITSHM=1" >> /etc/bash.bashrc  
  
# Entrypoint  
CMD /bin/bash  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

