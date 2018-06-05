FROM debian:wheezy  
MAINTAINER denLabo LLC  
  
# Install dependencies  
RUN apt-get update -q -y && apt-get install -y \  
build-essential g++ openjdk-7-jre unzip wget xz-utils libx11-6 libxext-dev
libxrender-dev libxtst-dev && \  
rm -rf /var/lib/apt/lists/*  
# Make a user  
ENV HOME /home/arduino  
ENV USER arduino  
RUN useradd --create-home --home-dir $HOME $USER  
WORKDIR $HOME  
  
# Add the default preferences  
ADD preferences.txt $HOME/.arduino15/  
ADD package_* $HOME/.arduino15/  
  
# Change the current user  
RUN chown -R $USER:$USER $HOME  
USER $USER  
  
# Install Arduino IDE  
RUN wget https://downloads.arduino.cc/arduino-1.6.7-linux64.tar.xz && \  
tar Jxf arduino-1.6.7-linux64.tar.xz -C ~/ && rm arduino-1.6.7-linux64.tar.xz
&& \  
chmod u+x ~/arduino-1.6.7/arduino && \  
mkdir ~/.bin/ && ln -s ~/arduino-1.6.7/arduino ~/.bin/arduino && \  
mkdir ~/Arduino/  
# Make the directories  
RUN mkdir ~/.tmp && mkdir -p ~/.arduino15/staging/packages/  
  
# Install - platforms - RedBearLab/nRF51822 Boards (32-bits ARM Cortex-M0)  
RUN wget https://redbearlab.github.io/arduino/nRF51822/nRF51822_board_v106.zip
-O ~/.arduino15/staging/packages/nRF51822_board_v106.zip && \  
mkdir -p ~/.arduino15/packages/RedBearLab/hardware/nRF51822/1.0.6/ && \  
unzip -q ~/.arduino15/staging/packages/nRF51822_board_v106.zip -d
~/.arduino15/packages/RedBearLab/hardware/nRF51822/  
# Install - tools - arduino/openocd  
RUN wget http://downloads.arduino.cc/tools/OpenOCD-0.9.0-arduino-x86_64-linux-
gnu.tar.bz2 -O
~/.arduino15/staging/packages/OpenOCD-0.9.0-arduino-x86_64-linux-gnu.tar.bz2
&& \  
mkdir -p ~/.arduino15/packages/arduino/tools/openocd/0.9.0-arduino/ && \  
tar xf ~/.arduino15/staging/packages/OpenOCD-0.9.0-arduino-x86_64-linux-
gnu.tar.bz2 -C ~/.tmp/ && \  
mv ~/.tmp/OpenOCD-0.9.0-dev-arduino/*
~/.arduino15/packages/arduino/tools/openocd/0.9.0-arduino/  
  
# Install - tools - RedBearLab/gcc  
RUN wget http://downloads.arduino.cc/gcc-arm-none-eabi-4.8.3-2014q1-mac.tar.gz
-O ~/.arduino15/staging/packages/gcc-arm-none-eabi-4.8.3-2014q1-mac.tar.gz &&
\  
mkdir -p ~/.arduino15/packages/RedBearLab/tools/arm-none-eabi-
gcc/4.8.3-2014q1/ && \  
tar xf ~/.arduino15/staging/packages/gcc-arm-none-eabi-4.8.3-2014q1-mac.tar.gz
-C ~/.tmp/ && \  
mv ~/.tmp/gcc-arm-none-eabi-4.8.3-2014q1/*
~/.arduino15/packages/RedBearLab/tools/arm-none-eabi-gcc/4.8.3-2014q1/  
  
# Install - tools - ReadBearLab/bossac  
RUN wget http://downloads.arduino.cc/tools/bossac-1.3a-arduino-x86_64-pc-
linux-gnu.tar.bz2 -O
~/.arduino15/staging/packages/bossac-1.3a-arduino-x86_64-pc-linux-gnu.tar.bz2
&& \  
mkdir -p ~/.arduino15/packages/RedBearLab/tools/bossac/1.3a-arduino/ && \  
tar xf ~/.arduino15/staging/packages/bossac-1.3a-arduino-x86_64-pc-linux-
gnu.tar.bz2 -C ~/.tmp/ && \  
mv ~/.tmp/bossac-1.3a-arduino/bossac
~/.arduino15/packages/RedBearLab/tools/bossac/1.3a-arduino/  
  
# Launch the IDE  
CMD ["/home/arduino/.bin/arduino"]  

