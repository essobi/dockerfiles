FROM ros:indigo-ros-base  
  
#update apt-get source list  
RUN apt-get update  
  
#install necessary packages  
RUN apt-get install -q -y g++ wget  
  
#install image processing related packages  
RUN apt-get install -q -y ros-indigo-rosjava \  
ros-indigo-camera-calibration-parsers \  
ros-indigo-ecl-command-line \  
ros-indigo-image-transport \  
ros-indigo-cv-bridge \  
ros-indigo-opencv3 \  
libzbar-dev \  
ros-indigo-tf2-ros \  
ros-indigo-mavros \  
ros-indigo-mavros-extras \  
ros-indigo-rosjava \  
ros-indigo-rqt-* \  
ros-indigo-rqt  
  
#install gazebo 7  
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable
`lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'  
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add
-  
RUN apt-get update  
RUN apt-get install -q -y gazebo7 libgazebo7-dev ros-indigo-gazebo7-ros  
  
#install px4 dev tools  
RUN apt-get install -q -y python-software-properties software-properties-
common  
RUN add-apt-repository -y ppa:george-edison55/cmake-3.x  
RUN apt-get update  
RUN apt-get install -y -q python-argparse \  
git-core \  
wget \  
zip \  
python-empy \  
qtcreator \  
cmake \  
build-essential \  
genromfs  
  
# install packages  
RUN apt-get install -q -y \  
build-essential \  
cmake \  
imagemagick \  
libboost-all-dev \  
libgts-dev \  
libjansson-dev \  
libtinyxml-dev \  
mercurial \  
nodejs \  
nodejs-legacy \  
npm \  
pkg-config \  
psmisc  
  
# clone gzweb  
RUN hg clone https://bitbucket.org/osrf/gzweb ~/gzweb  
  
# build gzweb  
RUN cd ~/gzweb \  
&& hg up default \  
&& ./deploy.sh -m  
  
#clone gazebo models  
RUN hg clone https://bitbucket.org/osrf/gazebo_models ~/models  
  
RUN cd ~/models \  
&& hg up default  
  
# #clone PX4 firmware  
# RUN git clone https://github.com/PX4/Firmware.git ~/Firmware  
# RUN cd ~/Firmware; git checkout v1.5.5 -b v1.5.5; git submodule update
--init --recursive  
# RUN apt-get install -q -y protobuf-compiler  
# RUN cd ~/Firmware; make posix_sitl_default  
# RUN mkdir -p ~/Firmware/build_gazebo  
# RUN cd ~/Firmware/build_gazebo; cmake ~/Firmware/Tools/sitl_gazebo; make  
#create and init catkin_ws  
RUN mkdir -p ~/catkin_ws/src  
RUN bash -c "source /opt/ros/indigo/setup.bash;catkin_init_workspace
~/catkin_ws/src"  
RUN bash -c "source /opt/ros/indigo/setup.bash;catkin_make -C ~/catkin_ws"  
  
# setup entrypoint  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]FROM ros:indigo-ros-base  
  
#update apt-get source list  
RUN apt-get update  
  
#install necessary packages  
RUN apt-get install -q -y g++ wget  
  
#install image processing related packages  
RUN apt-get install -q -y ros-indigo-rosjava \  
ros-indigo-camera-calibration-parsers \  
ros-indigo-ecl-command-line \  
ros-indigo-image-transport \  
ros-indigo-cv-bridge \  
ros-indigo-opencv3 \  
libzbar-dev \  
ros-indigo-tf2-ros \  
ros-indigo-mavros \  
ros-indigo-mavros-extras \  
ros-indigo-rosjava \  
ros-indigo-rqt-* \  
ros-indigo-rqt  
  
#install gazebo 7  
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable
`lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'  
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add
-  
RUN apt-get update  
RUN apt-get install -q -y gazebo7 libgazebo7-dev ros-indigo-gazebo7-ros  
  
# #install px4 dev tools  
# RUN apt-get install -q -y python-software-properties software-properties-
common  
# RUN add-apt-repository -y ppa:george-edison55/cmake-3.x  
# RUN apt-get update  
# RUN apt-get install -y -q python-argparse \  
# git-core \  
# wget \  
# zip \  
# python-empy \  
# qtcreator \  
# cmake \  
# build-essential \  
# genromfs  
# install packages  
RUN apt-get install -q -y \  
build-essential \  
cmake \  
imagemagick \  
libboost-all-dev \  
libgts-dev \  
libjansson-dev \  
libtinyxml-dev \  
mercurial \  
nodejs \  
nodejs-legacy \  
npm \  
pkg-config \  
psmisc  
  
# clone gzweb  
RUN hg clone https://bitbucket.org/osrf/gzweb ~/gzweb  
  
# build gzweb  
RUN cd ~/gzweb \  
&& hg up default \  
&& ./deploy.sh -m  
  
#clone gazebo models  
RUN hg clone https://bitbucket.org/osrf/gazebo_models ~/models  
  
RUN cd ~/models \  
&& hg up default  
  
# #clone PX4 firmware  
# RUN git clone https://github.com/PX4/Firmware.git ~/Firmware  
# RUN cd ~/Firmware; git checkout v1.5.5 -b v1.5.5; git submodule update
--init --recursive  
# RUN apt-get install -q -y protobuf-compiler  
# RUN cd ~/Firmware; make posix_sitl_default  
# RUN mkdir -p ~/Firmware/build_gazebo  
# RUN cd ~/Firmware/build_gazebo; cmake ~/Firmware/Tools/sitl_gazebo; make  
#create and init catkin_ws  
RUN mkdir -p ~/catkin_ws/src  
RUN bash -c "source /opt/ros/indigo/setup.bash;catkin_init_workspace
~/catkin_ws/src"  
RUN bash -c "source /opt/ros/indigo/setup.bash;catkin_make -C ~/catkin_ws"  
  
# setup entrypoint  
COPY ./entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]

