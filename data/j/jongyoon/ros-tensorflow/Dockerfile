FROM tensorflow/tensorflow:latest-gpu  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y --no-install-recommends --fix-missing \  
build-essential autoconf automake git \  
wget usbutils unzip vim \  
software-properties-common libxext-dev libxrender-dev libxslt1.1 libxtst-dev
libgtk2.0-0 libcanberra-gtk-module \  
locales && \  
locale-gen en_US.UTF-8  
  
# clion ide  
ENV CLION_VER=2017.2.1  
ENV CLION_HOME=/etc/clion  
RUN wget -nv https://download.jetbrains.com/cpp/CLion-${CLION_VER}.tar.gz -O
/tmp/clion.tar.gz && \  
mkdir ${CLION_HOME} && \  
tar -xzf /tmp/clion.tar.gz -C ${CLION_HOME} \--strip=1  
RUN sh -c 'echo "alias clion='${CLION_HOME}/bin/clion.sh'" >> ~/.bashrc'  
  
# pycharm idea  
ENV PYCHARM_VER=2017.2  
ENV PYCHARM_HOME=/etc/pycharm  
RUN wget -nv https://download.jetbrains.com/python/pycharm-
community-${PYCHARM_VER}.tar.gz -O /tmp/pycharm.tar.gz && \  
mkdir ${PYCHARM_HOME} && \  
tar -xzf /tmp/pycharm.tar.gz -C ${PYCHARM_HOME} \--strip=1  
RUN sh -c 'echo "alias pycharm='${PYCHARM_HOME}/bin/pycharm.sh'" >> ~/.bashrc'  
  
# ros-kinetic  
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc)
main" > /etc/apt/sources.list.d/ros-latest.list'  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ros-kinetic-desktop ros-kinetic-libuvc-camera ros-kinetic-image-view ros-
kinetic-cv-bridge ros-kinetic-cv-camera && \  
rm -rf /var/lib/apt/lists/*  
RUN rosdep init && \  
rosdep update  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
python-rosinstall python-rosinstall-generator python-wstool  
  
RUN mkdir -p ~/catkin_ws/src  
  
# download pylonsdk and get ready for installation  
RUN wget -nv https://www.dropbox.com/s/7yxzyudgdukicme/pylon-5.0.5.9000--
RC8-x86_64.tar.gz?dl=0 -O /tmp/pylon.tar.gz  
RUN tar -xzf /tmp/pylon.tar.gz -C /tmp  
RUN cd /tmp/pylon-5.0.5.9000-x86_64  
RUN tar -xzf /tmp/pylon-5.0.5.9000-x86_64/pylonSDK-5.0.5.9000-x86_64.tar.gz -C
/opt  
RUN sh -c 'echo "alias pylonviewer='/opt/pylon5/bin/PylonViewerApp'" >>
~/.bashrc'  
RUN sh -c 'echo "export QT_X11_NO_MITSHM=1" >> ~/.bashrc'  
  
# for ros environments  
# RUN sh -c 'echo "source '~/catkin_ws/devel/setup.bash'" >> ~/.bashrc'  
# RUN sh -c 'echo "source '/opt/ros/kinetic/setup.bash'" >> ~/.bashrc'  
# entrypoint  
COPY ./ros_entrypoint.sh /  
RUN chmod +x /ros_entrypoint.sh  
ENTRYPOINT ["/ros_entrypoint.sh"]  

