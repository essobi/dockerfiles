FROM debian:9  
# Most dependencies  
RUN apt-get update && \  
apt-get clean && \  
apt-get --fix-missing -y install \  
build-essential \  
cmake \  
libfftw3-3 \  
libfftw3-dev \  
gdb \  
libboost-all-dev \  
libhdf5-dev \  
librabbitmq-dev \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
## CMake  
#ARG CMAKEVER=3.6  
#ARG CMAKEINSTALLER=cmake-3.6.2-Linux-x86_64.sh  
#RUN wget https://cmake.org/files/v$CMAKEVER/$CMAKEINSTALLER && \  
# chmod u+x $CMAKEINSTALLER && \  
# ./$CMAKEINSTALLER --skip-license --prefix=/usr/local && \  
# rm $CMAKEINSTALLER  
#RUN mkdir /code  
#ADD psyllid /code/psyllid  
# note that the build dir is *not* in source, this is so that the source can
me mounted onto the container without covering the build target  
COPY dripline-cpp /usr/local/src/dripline-cpp  
COPY examples /usr/local/src/examples  
COPY external /usr/local/src/external  
COPY monarch /usr/local/src/monarch  
COPY midge /usr/local/src/midge  
COPY source /usr/local/src/source  
COPY CMakeLists.txt /usr/local/src/CMakeLists.txt  
  
RUN cd /usr/local/src && \  
mkdir -p build && \  
cd build && \  
cmake .. && \  
# unclear while I have to run cmake twice  
cmake -DPsyllid_ENABLE_TESTING=TRUE -DCMAKE_INSTALL_PREFIX:PATH=/usr/local
-DPsyllid_ENABLE_STREAMED_FREQUENCY_OUTPUT=TRUE . && \  
make -j2 install  
  
RUN cp /usr/local/src/examples/str_1ch_fpa.yaml /etc/psyllid_config.yaml  

