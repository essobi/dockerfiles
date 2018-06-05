# Start with the CUDA image from nvidia  
FROM nvidia/cuda:latest  
MAINTAINER Chris Watkins <christopher.watkins@me.com>  
  
# Install necessary ubuntu applications  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
wget \  
cmake \  
unzip \  
git \  
libatlas-base-dev  
  
# Download and install g3log  
RUN wget https://codeload.github.com/KjellKod/g3log/tar.gz/1.2 && \  
tar xvfz 1.2 && \  
cd g3log-1.2 && \  
mkdir build && \  
cd ./build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DUSE_DYNAMIC_LOGGING_LEVELS=ON .. && \  
make && \  
cp -r ../src/g3log /usr/local/include && \  
cp ./lib* /usr/local/lib && \  
cd ../../ && \  
rm -rf g3log-1.2 && \  
rm -f 1.2  
# Download and install pcg_rand  
RUN git clone https://github.com/imneme/pcg-c.git && \  
cd pcg-c && \  
make && \  
make test && \  
cp src/libpcg_random.a /usr/local/lib/ && \  
cp include/pcg_variants.h /usr/local/include/ && \  
cp -r extras /usr/local/include/ && \  
cd ../ && \  
rm -rf pcg-c  
  
# Download and install googletest  
RUN git clone https://github.com/google/googletest.git && \  
cd googletest && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
cp -a ../googletest/include/gtest /usr/include && \  
cp -a googlemock/gtest/libgtest_main.a /usr/lib/ && \  
cp -a googlemock/gtest/libgtest.a /usr/lib/ && \  
cd ../ && \  
rm -rf googletest  
  
  
# Download and install testu01  
RUN wget http://www.iro.umontreal.ca/~simardr/testu01/TestU01.zip && \  
unzip TestU01.zip && \  
cd TestU01* && \  
./configure && \  
make && \  
make install && \  
cd ../ && \  
rm -rf TestU01*  
  
RUN git clone https://github.com/inJeans/cuda_dsmc.git && \  
cd cuda_dsmc && \  
git checkout develop-2.0 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make  
  
CMD cd cuda_dsmc/build && \  
git checkout develop-2.0 && \  
git pull && \  
make clean && \  
make clean-cmake && \  
cmake .. && \  
make && \  
make test  
  
  
# Add the testu01 installation to the environment paths  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
ENV LIBRARY_PATH /usr/local/lib:$LIBRARY_PATH  
ENV C_INCLUDE_PATH /usr/local/include:$C_INCLUDE_PATH

