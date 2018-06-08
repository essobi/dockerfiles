FROM ubuntu:xenial  
RUN apt-get update && apt-get install -y build-essential git ssh libc6-i386  
ADD https://launchpad.net/gcc-arm-
embedded/4.9/4.9-2015-q3-update/+download/gcc-arm-none-
eabi-4_9-2015q3-20150921-linux.tar.bz2 /tmp  
RUN mkdir -p /usr/local && cd /usr/local && tar xjf /tmp/gcc-arm-none-
eabi-4_9-2015q3-20150921-linux.tar.bz2  

