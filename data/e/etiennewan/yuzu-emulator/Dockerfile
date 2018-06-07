FROM janx/ubuntu-dev  
MAINTAINER Selby "jselby@jselby.net"  
  
RUN sudo apt-get update -q \  
&& sudo apt-get install -y libqt5opengl5-dev libsdl2-dev libssl-dev
qtbase5-dev  
  
# We use a newer version of CMake then is provided by Ubuntu  
RUN wget https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.sh \  
&& mkdir /home/user/cmake \  
&& sh cmake-3.10.1-Linux-x86_64.sh \--exclude-subdir --prefix=/home/user/cmake
--skip-license  
ENV PATH="/home/user/cmake/bin:${PATH}"  
  
RUN git clone https://github.com/yuzu-emu/yuzu /home/user/yuzu \--recursive \  
&& mkdir /home/user/yuzu/build  
WORKDIR /home/user/yuzu/build  
  
# Build  
#RUN cmake .. -DYUZU_BUILD_UNICORN=ON -DCMAKE_BUILD_TYPE=Release \  
# && make -j4  
  
#RUN ctest -VV -C Release  
  
# Configure Cloud9 to use yuzu source directory as workspace (-w).  
RUN sudo sed -i "s/-w \/home\/user/-w \/home\/user\/yuzu/"
/etc/supervisord.conf  

