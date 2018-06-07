FROM debian:testing  
RUN sed -i "s/deb.debian.org/ftp.us.debian.org/" /etc/apt/sources.list  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y git build-essential zlib1g-dev libreadline-dev
libncurses-dev libxt-dev libopenmpi-dev openmpi-bin wget cmake gfortran python
bison flex python-pip lcov cppcheck python-dev libpython-dev  

