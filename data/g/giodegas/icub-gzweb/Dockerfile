FROM giodegas/gzweb  
MAINTAINER Giovanni De Gasperis giovanni@giodegas.it  
  
RUN sh -c 'echo "deb http://www.icub.org/ubuntu trusty contrib/science" >
/etc/apt/sources.list.d/icub.list'  
RUN apt-get update && apt-get upgrade -q -y  
RUN apt-get install -q -y --force-yes git yarp && yarp check  
  
RUN cd /root && git clone https://github.com/robotology/gazebo-yarp-
plugins.git  
  
# with disabled lasersensor  
COPY CMakeLists.txt /root/gazebo-yarp-plugins/plugins/CMakeLists.txt  
  
RUN cd /root/gazebo-yarp-plugins && \  
mkdir build && \  
cd build && \  
cmake ..&& \  
make install && \  
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:/usr/local  
  
RUN cd /root && git clone https://github.com/robotology/icub-gazebo.git && \  
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/root/icub-gazebo  
  
RUN cd /root/gzweb && \  
./deploy.sh -m -t  
  
# open port to interact with it  
EXPOSE 10000/tcp  

