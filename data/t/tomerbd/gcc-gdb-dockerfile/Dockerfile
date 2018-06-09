FROM ubuntu  
RUN sudo apt-get -y install software-properties-common  
RUN sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN sudo apt-get update  
RUN sudo apt-get -y install gcc-4.9 g++-4.9  
RUN sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60
--slave /usr/bin/g++ g++ /usr/bin/g++-4.9  
RUN sudo apt-get -y install build-essential  
RUN sudo apt-get -y install libc6-dbg gdb valgrind  
CMD ["/bin/bash"]  

