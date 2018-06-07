FROM debian  
RUN sed -i "s/httpredir/ftp.us/" /etc/apt/sources.list  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y git build-essential zlib1g-dev libreadline-dev
libncurses-dev libxt-dev libopenmpi-dev openmpi-bin wget cmake petsc-dev
gfortran python bison flex python-pip lcov cppcheck python-dev libpython-dev  

