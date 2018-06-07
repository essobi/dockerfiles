FROM ubuntu:xenial  
  
ENV CC /usr/bin/gcc-4.9  
ENV CXX /usr/bin/g++-4.9  
RUN apt-get update  
RUN apt-get install -y sudo  
RUN sudo apt-get update  
RUN sudo apt-get install -y git  
RUN git clone https://github.com/internetofvehicles/ENCODERS  
ARG CACHEBUST=1  
RUN cd ENCODERS && git pull  
RUN cd ENCODERS && ./build_haggle.sh  
  
#make directories and set permissions in container  
RUN sudo useradd -d /home/ubuntu ubuntu  
RUN sudo mkdir -p /home/ubuntu/.Haggle  
RUN sudo chown -R ubuntu:ubuntu /home/ubuntu  
  
RUN sudo apt-get install -y vim  
  
#networking tools in conainer  
RUN sudo apt-get install -y iputils-ping net-tools telnet netcat  
  
#add some haggle config  
ADD config-udptcp.xml /home/ubuntu/.Haggle/config.xml  
  
#make sure owner of home and haggle folder are set (not root)  
RUN sudo chown -R ubuntu:ubuntu /home/ubuntu  
  
ADD starthaggle.sh /starthaggle.sh  

