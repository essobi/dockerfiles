FROM ubuntu:12.04  
MAINTAINER Furushchev <furushchev@mail.ru>  
  
RUN sed -i".bak" -e 's/\/\/archive.ubuntu.com/\/\/ftp.jaist.ac.jp/g'
/etc/apt/sources.list  
RUN apt-get -q update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y apt-utils  
RUN apt-get upgrade -y  
  
# locale  
RUN apt-get install -y --no-install-recommends locales language-pack-ja  
RUN locale-gen ja_JP.UTF-8  
RUN locale-gen en_US.UTF-8  
#RUN update-locale LANG=en_JP.UTF-8  
RUN dpkg-reconfigure locales  
ENV LANG ja_JP.UTF-8  
ENV DEBIAN_FRONTEND noninteractive LANG  
  
  
# minimum installation  
RUN apt-get install -y software-properties-common ssh sudo wget curl
emacs23-nox nginx lsb-release  
  
# add rosuser user  
ENV USERNAME rosuser  
ENV HOME /home/$USERNAME  
RUN mkdir -p $HOME  
RUN useradd $USERNAME  
RUN echo "$USERNAME:$USERNAME" | chpasswd  
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN chown -R $USERNAME:$USERNAME $HOME  
  
RUN mkdir -p $HOME/.ssh; chown $USERNAME $HOME/.ssh; chmod 0700 $HOME/.ssh  
ADD authorized_keys $HOME/.ssh/  
ADD authorized_keys /root/.ssh/  
RUN service ssh restart  
EXPOSE 22  
# change user  
USER rosuser  
WORKDIR /home/rosuser/  
  
# setup vnc  
RUN sudo apt-get install -y x11vnc xvfb firefox  
RUN mkdir $HOME/.vnc  
RUN x11vnc -storepasswd 1234 $HOME/.vnc/passwd  
  
# install ros  
RUN wget -q -O /tmp/jsk.rosbuild https://raw.github.com/jsk-ros-
pkg/jsk_common/master/jsk.rosbuild  
RUN sed -i".bak" -e 's/rosws update/rosws update -j100/g' /tmp/jsk.rosbuild  
RUN yes p | bash /tmp/jsk.rosbuild groovy setup-ros  
RUN yes p | bash /tmp/jsk.rosbuild groovy install-jsk-ros-pkg  
RUN yes p | bash /tmp/jsk.rosbuild groovy compile-jsk-ros-pkg  
RUN yes p | bash /tmp/jsk.rosbuild groovy test-jsk-ros-pkg  
  
# remove nopasswd for rosuser  
USER root  
RUN sed -e 's/NOPASSWD:ALL/ALL/g' /etc/sudoers  
USER rosuser  
  
RUN echo "source $HOME/ros/groovy/setup.bash" >> $HOME/.bashrc  
  
ENTRYPOINT "/bin/bash"  

