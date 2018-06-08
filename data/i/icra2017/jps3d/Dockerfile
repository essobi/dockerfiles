FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
build-essential git \  
libeigen3-dev libyaml-cpp-dev libboost-dev cmake \  
&& rm -rf /var/lib/apt/lists  
  
RUN git clone -b reproducible https://github.com/ICRA2017/jps3d.git  
  
RUN cd jps3d && mkdir build && cd build \  
&& cmake .. && make -j4  
  
RUN cd jps3d/build && make test  
  
CMD ["/jps3d/build/test_planner_2d", "/jps3d/data/corridor.yaml"]  

