FROM ubuntu:bionic  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get -y install build-essential vim-common wget git bzip2
make python libc6:i386 astyle clang cmake && \  
apt-get -y install python3 python3-pip &&\  
pip3 install --user pipenv && \  
wget https://launchpad.net/gcc-arm-
embedded/5.0/5-2016-q2-update/+download/gcc-arm-none-
eabi-5_4-2016q2-20160622-linux.tar.bz2 && \  
wget https://launchpad.net/gcc-arm-
embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-
eabi-5_4-2016q3-20160926-linux.tar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-
rm/5_3-2016q1/gccarmnoneeabi532016q120160330linuxtar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-
rm/5_4-2016q2/gccarmnoneeabi542016q220160622linuxtar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/5_4-2016q3/gcc-
arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/6-2016q4/gcc-
arm-none-eabi-6_2-2016q4-20161216-linux.tar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/6_1-2017q1/gcc-
arm-none-eabi-6-2017-q1-update-linux.tar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/6-2017q2/gcc-
arm-none-eabi-6-2017-q2-update-linux.tar.bz2 && \  
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/7-2017q4/gcc-
arm-none-eabi-7-2017-q4-major-linux.tar.bz2 && \  
mkdir -p /usr/local/bin/ && \  
tar -xf gcc-arm-none-eabi-5_4-2016q2-20160622-linux.tar.bz2 -C /usr/local/bin/
&& \  
tar -xf gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 -C /usr/local/bin/
&& \  
tar -xf gccarmnoneeabi532016q120160330linuxtar.bz2 -C /usr/local/bin/ && \  
tar -xf gccarmnoneeabi542016q220160622linuxtar.bz2 -C /usr/local/bin/ && \  
tar -xf gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 -C /usr/local/bin/
&& \  
tar -xf gcc-arm-none-eabi-6_2-2016q4-20161216-linux.tar.bz2 -C /usr/local/bin/
&& \  
tar -xf gcc-arm-none-eabi-6-2017-q1-update-linux.tar.bz2 -C /usr/local/bin/ &&
\  
tar -xf gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2 -C /usr/local/bin/ &&
\  
tar -xf gcc-arm-none-eabi-7-2017-q4-major-linux.tar.bz2 -C /usr/local/bin/  
  

