FROM shawnchang420/cuda-drl  
LABEL name="roboschool"  
LABEL description="With Roboschool dependencies installed"  
LABEL authors="Shawn Chang <ebola777@yahoo.com.tw>"  
  
################################################################################  
# Install Roboschool dependencies  
# Reference: https://github.com/openai/roboschool  
################################################################################  
# Specify the installation path  
ARG INSTALL_PATH=/usr/local  
  
# Install the dependencies  
RUN apt -y install \  
ffmpeg pkg-config \  
qtbase5-dev \  
libqt5opengl5-dev \  
libassimp-dev \  
libpython3.5-dev \  
libboost-python-dev \  
libtinyxml-dev  
  
# Install Bullet  
# Go to the temporary directory  
RUN cd /tmp/ && \  
# Clone the repository  
git clone https://github.com/olegklimov/bullet3 -b roboschool_self_collision
&& \  
# Create the build directory  
mkdir bullet3/build && \  
# Go to the build directory  
cd bullet3/build && \  
# Build Bullet  
cmake -DBUILD_SHARED_LIBS=ON -DUSE_DOUBLE_PRECISION=1
-DCMAKE_INSTALL_PREFIX:PATH=$INSTALL_PATH/roboschool/cpp-
household/bullet_local_install -DBUILD_CPU_DEMOS=OFF -DBUILD_BULLET2_DEMOS=OFF
-DBUILD_EXTRAS=OFF -DBUILD_UNIT_TESTS=OFF -DBUILD_CLSOCKET=OFF
-DBUILD_ENET=OFF -DBUILD_OPENGL3_DEMOS=OFF .. && \  
make -j4 && \  
make install && \  
# Remove the repository  
rm -rf /tmp/bullet3

