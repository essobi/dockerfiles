FROM osrf/ros:kinetic-desktop-full-xenial  
  
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
  
# jdk8  
# RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
# RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-
set-selections  
#  
# RUN apt-get update && \  
# apt-get install -y --no-install-recommends software-properties-common && \  
# add-apt-repository ppa:webupd8team/java && \  
# apt-get update && \  
# apt-get install -y --no-install-recommends oracle-java8-installer && \  
# rm -rf /var/lib/apt/lists/*  
# jdk7  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN wget -nv
https://www.dropbox.com/s/y3ukn4t60welhba/jdk-7u80-linux-x64.tar.gz?dl=0 -O
/tmp/jdk-7u80-linux-x64.tar.gz  
RUN echo oracle-java7-installer oracle-java7-installer/local select /tmp |
/usr/bin/debconf-set-selections  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y --no-install-recommends oracle-java7-installer  
RUN update-java-alternatives -s java-7-oracle  
  
# idea  
ENV IDEA_VER=2017.2.2  
ENV IDEA_HOME=/etc/idea  
RUN wget -nv https://download.jetbrains.com/idea/ideaIC-${IDEA_VER}.tar.gz -O
/tmp/idea.tar.gz && \  
mkdir ${IDEA_HOME} && \  
tar -xzf /tmp/idea.tar.gz -C ${IDEA_HOME} \--strip=1  
RUN echo "alias idea_launcher='${IDEA_HOME}/bin/idea.sh'" >> ~/.bashrc  
RUN echo "alias idea='idea_launcher > /dev/null 2>&1 &'" >> ~/.bashrc  
  
# clion  
ENV CLION_VER=2017.2.1  
ENV CLION_HOME=/etc/clion  
RUN wget -nv https://download.jetbrains.com/cpp/CLion-${CLION_VER}.tar.gz -O
/tmp/clion.tar.gz && \  
mkdir ${CLION_HOME} && \  
tar -xzf /tmp/clion.tar.gz -C ${CLION_HOME} \--strip=1  
RUN echo "alias clion_launcher='${CLION_HOME}/bin/clion.sh'" >> ~/.bashrc  
RUN echo "alias clion='clion_launcher > /dev/null 2>&1 &'" >> ~/.bashrc  
  
# pycharm  
ENV PYCHARM_VER=2017.2  
ENV PYCHARM_HOME=/etc/pycharm  
RUN wget -nv https://download.jetbrains.com/python/pycharm-
community-${PYCHARM_VER}.tar.gz -O /tmp/pycharm.tar.gz && \  
mkdir ${PYCHARM_HOME} && \  
tar -xzf /tmp/pycharm.tar.gz -C ${PYCHARM_HOME} \--strip=1  
RUN echo "alias pycharm_launcher='${PYCHARM_HOME}/bin/pycharm.sh'" >>
~/.bashrc  
RUN echo "alias pycharm='pycharm_launcher > /dev/null 2>&1 &'" >> ~/.bashrc  
  
# rosjava  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ros-kinetic-rosjava  
  
# ros bridge  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ros-kinetic-rosbridge-server  
  
# catkin workspace  
RUN mkdir -p ~/catkin_ws/src  
  
RUN echo "alias cm='cd ~/catkin_ws && catkin_make'" >> ~/.bashrc  
RUN echo "alias cw='cd ~/catkin_ws'" >> ~/.bashrc  
RUN echo "export ROS_MASTER_URI=http://172.22.0.79:11311" >> ~/.bashrc  
RUN echo "export ROS_HOSTNAME=130.216.119.131" >> ~/.bashrc  
  
# dependencies for healthcare project  
RUN easy_install pip  
RUN pip install humanize requests  
  
# chrome browser  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends google-chrome-stable  
  
# for ros environments  
# RUN sh -c 'echo "source '~/catkin_ws/devel/setup.bash'" >> ~/.bashrc'  
# RUN sh -c 'echo "source '/opt/ros/kinetic/setup.bash'" >> ~/.bashrc'  
# entrypoint  
COPY ./ros_entrypoint.sh /  
RUN chmod +x /ros_entrypoint.sh  
ENTRYPOINT ["/ros_entrypoint.sh"]  
CMD ["bash"]  

