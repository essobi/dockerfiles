FROM debian:jessie  
MAINTAINER matt.trentini@gmail.com  
  
  
RUN apt-get update  
RUN apt-get install -y git \  
wget \  
make \  
libncurses-dev \  
flex \  
bison \  
gperf \  
python \  
python-serial  
  
# Note that the ESP documentation talks about installing to $HOME/esp...  
# http://esp-idf.readthedocs.io/en/latest/get-started/linux-setup.html  
# Only covers step 1 and 2. Beyond that is not necessary for Micropython  
RUN mkdir /esp  
WORKDIR /esp  
RUN wget https://dl.espressif.com/dl/xtensa-esp32-elf-
linux64-1.22.0-61-gab8375a-5.2.0.tar.gz  
RUN tar -xzf xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz  
RUN export PATH=$PATH:/esp/xtensa-esp32-elf/bin  
  
# Create a directory to store the code  
RUN mkdir /esp32-micropython  
WORKDIR /esp32-micropython/  
  
# Clone Expressif's ESP IDF  
RUN git clone \--recursive https://github.com/espressif/esp-idf.git  
WORKDIR /esp32-micropython/esp-idf  
# Checkout the latest supported ESP IDF  
RUN git checkout 4ec2abbf23084ac060679e4136fa222a2d0ab0e8  
# Export the location of the IDF so Micropython knows where to find it  
ENV ESPIDF=/esp32-micropython/esp-idf  
  
# Now for the ESP32 Micropython port  
WORKDIR /esp32-micropython/  
# https://github.com/micropython/micropython-esp32/tree/esp32/esp32  
RUN git clone https://github.com/micropython/micropython-esp32.git  
WORKDIR /esp32-micropython/micropython-esp32  
RUN make -C mpy-cross  
RUN git submodule init lib/berkeley-db-1.xx  
RUN git submodule update  
WORKDIR /esp32-micropython/micropython-esp32/esp32  
  
# Build the firmware  
# Binaries can be found: /esp32-micropython/micropython-esp32/esp32/build  
ENV PATH=$PATH:/esp/xtensa-esp32-elf/bin  
  
RUN make  

