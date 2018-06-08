FROM ubuntu:saucy  
RUN apt-get update  
RUN apt-get install -y build-essential ccache git cmake zlib1g-dev libboost-
dev libboost-filesystem-dev libboost-program-options-dev libboost-system-dev
libboost-thread-dev libpcap-dev libpcre3-dev libssl-dev libreadline-dev
debhelper devscripts buildbot-slave valgrind  
WORKDIR /data  
CMD buildslave start && tail -f twistd.log  

