FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# built-in packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common curl
\  
&& sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >>
/etc/apt/sources.list.d/arc-theme.list" \  
&& curl -SL
http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
| apt-key add - \  
&& add-apt-repository ppa:fcwu-tw/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --allow-unauthenticated \  
supervisor \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
lxde x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
firefox \  
nginx \  
python-pip python-dev build-essential \  
mesa-utils libgl1-mesa-dri \  
gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme
\  
dbus-x11 x11-utils \  
terminator \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
# =================================  
# install ros (source:
https://github.com/osrf/docker_images/blob/5399f380af0a7735405a4b6a07c6c40b867563bd/ros/kinetic/ubuntu/xenial/ros-
core/Dockerfile)  
# install packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
dirmngr \  
gnupg2 \  
&& rm -rf /var/lib/apt/lists/*  
# setup keys  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
# setup sources.list  
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list  
  
# install bootstrap tools  
RUN apt-get update && apt-get install --no-install-recommends -y \  
python-rosdep \  
python-rosinstall \  
python-vcstools \  
&& rm -rf /var/lib/apt/lists/*  
# setup environment  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# bootstrap rosdep  
RUN rosdep init \  
&& rosdep update  
  
# install ros packages  
ENV ROS_DISTRO kinetic  
RUN apt-get update && apt-get install -y \  
# ros-kinetic-ros-core=1.3.1-0* \  
ros-kinetic-desktop-full=1.3.1-0* \  
# A  
# +--- full desktop \  
&& rm -rf /var/lib/apt/lists/*  
# setup entrypoint  
# COPY ./ros_entrypoint.sh /  
# =================================  
# user tools  
RUN apt-get update && apt-get install -y \  
terminator \  
gedit \  
okular \  
&& rm -rf /var/lib/apt/lists/*  
# tini for subreap  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
  
ADD image /  
RUN pip install setuptools wheel && pip install -r
/usr/lib/web/requirements.txt  
  
RUN cp /usr/share/applications/terminator.desktop /root/Desktop  
RUN echo "source /opt/ros/kinetic/setup.bash" >> /root/.bashrc  
  
EXPOSE 80  
WORKDIR /root  
ENV HOME=/home/ubuntu \  
SHELL=/bin/bash  
ENTRYPOINT ["/startup.sh"]  

