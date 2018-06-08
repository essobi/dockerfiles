FROM jenkins:latest  
MAINTAINER Mike Müller <mike@objektarium.de>  
  
ENV REFRESHED_AT 2018-03-06  
USER root  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
  
# add sudo to the image  
RUN apt-get update \  
&& apt-get install -y sudo \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# add pharo-vm / build prerequisites  
RUN dpkg --add-architecture i386  
RUN apt-get update  
  
RUN apt-get install -y curl libc-bin libc-dev-bin libc6-dev  
RUN apt-get -yq --no-install-suggests --no-install-recommends --force-yes
install lib32z1 lib32ncurses5 gvfs-daemons:i386 cmake zip bash-completion git
xz-utils debhelper devscripts libc6-dev:i386 libasound2:i386
libasound2-dev:i386 libssl-dev:i386 libfreetype6-dev:i386 libx11-dev:i386
libsm-dev:i386 libice-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev:i386
libxext-dev:i386 libglapi-mesa:i386 build-essential gcc-multilib g++  
  
RUN curl -sSL https://get.docker.com/ | sh  
RUN usermod -a -G staff,docker jenkins  
  
# switch back to user jenkins  
USER jenkins  

