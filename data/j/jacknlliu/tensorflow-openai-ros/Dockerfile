FROM jacknlliu/tensorflow-openai-ros:origin-py3  
  
LABEL maintainer="Jack Liu <jacknlliu@gmail.com>"  
  
USER root  
  
# setup environment  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -f -y --no-install-recommends && apt-
get install -y -q --no-install-recommends apt-transport-https aptitude locales
&& locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
# define tini version  
ENV TINI_VERSION v0.17.0  
# define ros distribution version  
ENV ROS_DISTRO kinetic  
  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list \  
\  
# setup keys  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 \--recv-key
421C365BD9FF1F717815A3895523BAEEB01FA116 \  
\  
# update the repository and install ros kinetic  
&& aptitude update -y -q && aptitude install -y -q -R ros-kinetic-ros-base
python-rosinstall ninja-build python3-pip python3-setuptools \  
python3-defusedxml python3-dev \  
ros-kinetic-gazebo-msgs ros-kinetic-rosbridge-library \  
ros-kinetic-rosbridge-server ros-kinetic-rosbridge-suite  
  
# install ros python3 support  
RUN pip3 install --upgrade pip virtualenv && pip3 install --no-cache-dir
catkin-tools rospkg ws4py transforms3d trollius  
  
# install dependecies for ros genmsg using pip2  
RUN pip install empy  
  
# install additional system packages and ros packages  
# install additional build tool  
RUN aptitude install -y -q -R build-essential gdb tmux \  
\  
# install IDE essential packages and qt5, qtcreator, qtdeclarative5-qtquick2  
&& aptitude install -y -q -R mesa-common-dev libglu1-mesa-dev libfontconfig1
qt5-default qtcreator qtdeclarative5-qtquick2-plugin \  
\  
# install intel graphics driver  
&& aptitude install -y -q -R libgl1-mesa-glx libgl1-mesa-dri \  
\  
# install amd graphics open source driver  
&& aptitude install -y -q -R mesa-vdpau-drivers xserver-xorg-video-ati mesa-
utils module-init-tools  
  
# install RoboWare  
RUN aptitude install -y -q -R wget python-pip pylint clang libxss1 libnss3
libnotify4 libxtst6 ~nlibgconf-2 \  
&& export ROBOWAREVERSION="1.1.0-1514335284" \  
&& wget https://github.com/tonyrobotics/RoboWare/raw/master/Studio/roboware-
studio_${ROBOWAREVERSION}_amd64.deb -O roboware_amd64.deb \  
&& chmod a+x roboware_amd64.deb && dpkg -i roboware_amd64.deb \  
&& apt-get install -y --no-install-recommends -f \  
&& rm -f roboware_amd64.deb  
  
# install essential tools, ssh sever, sudo  
RUN aptitude update -y -q && aptitude install -y -q -R bash-completion wget
vim git iputils-ping iproute2 netcat terminator xauth openssh-server sudo
pcmanfm  
  
# install ros related components  
RUN aptitude install -y -q -R ros-kinetic-controller-manager \  
ros-kinetic-tf ros-kinetic-urdf \  
ros-kinetic-ros-controllers \  
ros-kinetic-hardware-interface \  
ros-kinetic-orocos-kdl \  
ros-kinetic-orocos-kinematics-dynamics \  
ros-kinetic-pid \  
\  
# install Barret_Hand related components  
&& aptitude install -y -q -R libignition-math2-dev \  
\  
# install kinematics module  
&& aptitude install -y -q -R ros-kinetic-calibration-estimation ros-kinetic-
kdl-parser-py \  
\  
# install fast inverse kinematics module  
&& aptitude install -y -q -R ros-kinetic-trac-ik-lib  
  
  
# install machine learning packages  
RUN mkdir -p /opt/scripts/container/ && chmod -R a+rx /opt/scripts/ \  
&& cd /opt/scripts/container/ && pip3 install
git+https://github.com/AlexanderFabisch/gmr.git  
  
# copy entrypoint file  
COPY ./scripts/*.sh ./config/requirements*.txt /opt/scripts/container/  
  
# config sshd  
RUN mkdir -p /var/run/sshd && echo "X11UseLocalhost no" >>
/etc/ssh/sshd_config  
  
RUN chmod a+rwx /opt/scripts/container/ros_entrypoint.sh
/opt/scripts/container/containerinit.sh \  
/opt/scripts/container/tensorflow-models.sh && sync &&
/opt/scripts/container/tensorflow-models.sh  
  
# add jupyter notebook tools  
RUN pip3 install nbmerge nbdime  
  
# set user ros and sudo  
RUN adduser --gecos "ROS User" \--home /home/ros --disabled-password ros && \  
usermod -a -G dialout ros && \  
echo "ros ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/99_aptget  
  
# setup ros env  
USER ros  
RUN sudo rosdep init && rosdep update \  
&& mkdir -p /home/ros/.local/lib/python2.7/site-packages \  
&& echo "/opt/ros/$ROS_DISTRO/lib/python2.7/dist-packages" >>
/home/ros/.local/lib/python2.7/site-packages/ros-dev.pth \  
&& mkdir -p /home/ros/.local/lib/python3.5/site-packages \  
&& echo -e "/opt/tensorflow-models/research\n/opt/tensorflow-
models/research/slim" >> /home/ros/.local/lib/python3.5/site-
packages/tensorflow-models.pth  
  
# install openai/baselines, roboschool, gym related python packages  
RUN sudo chmod +x /opt/scripts/container/dart_drl.sh
/opt/scripts/container/requirements*.txt && \  
sudo /opt/scripts/container/dart_drl.sh  
  
# configure Qt  
RUN mkdir -p /home/ros/.config/QtProject  
  
USER root  
  
# aptitude clean and installation scripts clean  
RUN apt-get autoclean \  
&& apt-get clean all \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /opt/scripts/container/tensorflow-models.sh
/opt/scripts/container/dart_drl.sh  
  
COPY ./config/QtCreator.ini /home/ros/.config/QtProject/  
RUN chown -R ros:users /home/ros/.config/QtProject/  
  
# config gazebo volume  
RUN mkdir -p /home/ros/.gazebo/models && chown -R ros:users /home/ros/.gazebo
\  
&& mkdir /home/ros/.jupyter \  
&& cp -f /root/.jupyter/jupyter_notebook_config.py /home/ros/.jupyter/ \  
&& chown -R ros:users /home/ros/.jupyter \  
&& chmod 755 /home/ros/.jupyter/jupyter_notebook_config.py  
  
# Add Tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
# Configure container startup, '-v' is needed, please see [using-
tini](https://github.com/krallin/tini#using-tini)  
ENTRYPOINT ["tini", "-v", "--", "/opt/scripts/container/ros_entrypoint.sh"]  
CMD ["bash"]  
  
USER ros  
WORKDIR /home/ros  

