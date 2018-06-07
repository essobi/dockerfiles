FROM ubuntu:xenial  
  
ENV ROS_DISTRO lunar  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
  
ADD http://osrf-
distributions.s3.amazonaws.com/gazebo/releases/gazebo-9.0.0.tar.bz2
/tmp/gazebo-source.tar.bz2  
COPY force-preserveWorldVelocity-true.patch /tmp/  
  
ENV DISPLAY :1  
  
COPY . yamax/  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends xvfb x11vnc fluxbox build-
essential psmisc dirmngr curl ca-certificates gnupg \  
&& echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116 \  
&& echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable xenial
main" > /etc/apt/sources.list.d/gazebo-stable.list \  
&& curl http://packages.osrfoundation.org/gazebo.key | apt-key add \- \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y python-rosdep python-rosinstall
python-vcstools \  
&& rosdep init \  
&& rosdep update \  
&& easy_install pip \  
&& pip install tensorflow==1.3.0 keras==2.0.6 keras-rl h5py gym \  
&& apt-get install -y \--no-install-recommends ros-lunar-ros-core=1.3.1-0*
ros-lunar-ros-base=1.3.1-0* xauth ros-lunar-joint-state-publisher ros-lunar-
rviz ros-lunar-robot-state-publisher ros-lunar-gazebo9-ros-pkgs ros-lunar-
gazebo9-ros-control ros-lunar-ros-controllers ros-lunar-ros-control ros-lunar-
joint-state-controller ros-lunar-position-controllers ros-lunar-xacro \  
&& cd /tmp \  
&& curl https://bitbucket.org/osrf/release-tools/raw/default/jenkins-
scripts/lib/dependencies_archive.sh > dependencies.sh \  
&& bash -c "ROS_DISTRO=lunar . ./dependencies.sh && apt-get install --no-
install-recommends -y \$(sed 's:\\\\\\\ ::g' <<< \$BASE_DEPENDENCIES) \$(sed
's:\\\\\\\ ::g' <<< \$GAZEBO_BASE_DEPENDENCIES_NO_SDFORMAT) libsdformat6-dev"
\  
&& tar xf /tmp/gazebo-source.tar.bz2 \  
&& cd gazebo-9.0.0 \  
&& patch -p1 < /tmp/force-preserveWorldVelocity-true.patch \  
&& mkdir build \  
&& cd build \  
&& cmake .. \  
&& make -j 4 \  
&& make package \  
&& apt-get purge -y curl build-essential \  
&& apt-get autoremove -y \  
&& dpkg -r --force-depends gazebo9 libgazebo9 libgazebo9-dev \  
&& dpkg -i --force-depends --force-overwrite
/tmp/gazebo-9.0.0/build/gazebo-9.0.0.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /tmp \  
&& git clone https://github.com/erlerobot/gym-gazebo.git \  
&& cd gym-gazebo \  
&& pip install -e . \  
&& rm -rf /tmp/* \  
&& rm -rf yamax/devel yamax/build \  
&& . /opt/ros/lunar/setup.sh \  
&& cd yamax \  
&& catkin_make \  
&& echo '. /opt/ros/lunar/setup.sh' >> /etc/profile \  
&& echo '. /yamax/devel/setup.sh' >> /etc/profile  
  
WORKDIR /yamax  
  
COPY ./vnc-startup.sh /  
EXPOSE 5900  
  
CMD bash -i -c "/vnc-startup.sh && roslaunch yamax_gazebo world.launch
gui:=True headless:=False"  

