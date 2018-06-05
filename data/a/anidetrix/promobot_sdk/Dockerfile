FROM ubuntu:14.04  
LABEL maintainer "Anidetrix <anton@anidetrix.ru>"  
# Add project source  
WORKDIR /proj  
VOLUME /proj  
VOLUME /install/plugins  
# Add required sources  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 38FBCCD3 E9977759
\  
&& echo "deb http://promobotvpn.cloudapp.net/repository/public/v3 trusty non-
free" > /etc/apt/sources.list.d/promobot.list \  
&& echo "deb http://promobotvpn.cloudapp.net/repository/public/ros trusty
main" >> /etc/apt/sources.list.d/promobot.list \  
&& echo "deb http://ppa.launchpad.net/beineri/opt-qt562-trusty/ubuntu trusty
main" > /etc/apt/sources.list.d/qt56.list \  
# Install dependencies  
&& apt-get update \  
&& apt-get -y install \  
# Install G++  
g++ \  
# Install GL lib  
libgl1-mesa-dev \  
# Install QT  
qt56-meta-full \  
# Install ROS  
ros-indigo-ros-base \  
# Install Promobot SDK libs  
promobot3-qt-libpromobot \  
promobot3-qt-libpromobot-dev \  
promobot3-qt-libpromobotwidgets \  
promobot3-qt-libpromobotwidgets-dev \  
promobot3-qt-libapplicationbase \  
promobot3-qt-libapplicationbase-dev \  
promobot3-qt-libapplicationwidgets \  
promobot3-qt-libapplicationwidgets-dev \  
promobot3-qt-PromobotDialogModule \  
promobot3-qt-PromobotDialogModule-dev \  
promobot3-qt-PromobotMainScreen \  
promobot3-qt-PromobotMainScreen-dev \  
# Cleanup  
&& rm -rf /var/lib/apt/lists/*  
# Set build script  
ENTRYPOINT ["/bin/bash", "Dockerbuild"]  

