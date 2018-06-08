FROM ubuntu:quantal  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y 'deb http://ppa.launchpad.net/kalakris/cmake/ubuntu
precise main'  
RUN apt-get update  
RUN apt-get install -y build-essential ccache git gcc-4.7 g++-4.7 cmake
zlib1g-dev libboost-dev libboost-filesystem-dev libboost-program-options-dev
libboost-system-dev libboost-thread-dev libpcap-dev libpcre3-dev libreadline-
dev debhelper devscripts buildbot-slave valgrind  
WORKDIR /data  
CMD buildslave start && tail -f twistd.log  

