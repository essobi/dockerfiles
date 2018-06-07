FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
build-essential git \  
&& rm -rf /var/lib/apt/lists  
  
RUN git clone -b reproducible https://github.com/ICRA2017/MSGD.git  
  
RUN cd MSGD && make all  

