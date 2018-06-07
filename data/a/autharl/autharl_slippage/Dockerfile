FROM ros:indigo  
  
MAINTAINER Ioannis Agriomallos <ioannis.agriomallos@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential sudo wget  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Create catkin workspace  
ENV CATKIN_WS=/root/catkin_ws  
RUN . /opt/ros/indigo/setup.bash && \  
mkdir -p $CATKIN_WS/src && cd $CATKIN_WS/src && catkin_init_workspace && \  
cd $CATKIN_WS && catkin_make && . $CATKIN_WS/devel/setup.bash  
  
# Build the code, run tests and run linter  
ENTRYPOINT . /opt/ros/indigo/setup.bash && \  
cd $CATKIN_WS/src/autharl_slippage/autharl_core && \  
apt-get install -y linux-headers-$(uname -r) && \  
./install.sh -a && \  
cd $CATKIN_WS/src/autharl_slippage/slippage_detection && \  
./setup.sh && \  
. $CATKIN_WS/devel/setup.bash && cd $CATKIN_WS && \  
catkin_make && \  
catkin_make run_tests && catkin_test_results && \  
. $CATKIN_WS/devel/setup.bash &&
./src/autharl_slippage/slippage_detection/scripts/test.py && \  
catkin_make roslint  

