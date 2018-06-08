FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -qy scons libevent-dev gengetopt libzmq-dev git g++  
RUN git clone https://github.com/leverich/mutilate.git  
  
WORKDIR mutilate  
  
RUN scons  

