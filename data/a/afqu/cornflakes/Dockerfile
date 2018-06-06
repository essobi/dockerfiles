# Use an official Python runtime as a parent image  
FROM debian:latest  
  
RUN apt-get update  
RUN apt-get -y install cmake make g++ gfortran git python  
RUN apt-get -y install libblas-dev liblapack-dev  
RUN apt-get -y install openmpi-bin openmpi-common libopenmpi-dev libopenmpi2  
RUN apt-get -y install swig python-numpy python-scipy python-matplotlib
python-sympy  
RUN apt-get -y install ipython  
RUN apt-get -y install libgsl-dev  
RUN apt-get -y install python-pip  
  
RUN pip install oset  
  
# Set the working directory  
WORKDIR /opt_cornflakes  
  
# Copy the current directory contents into the container at /app  
ADD . /opt_cornflakes/source  
  
RUN mkdir -p build ; \  
cd build ; \  
cmake ../source/superbuild/ ; \  
make  
  
# Download some fun examples  
RUN git clone https://github.com/afqueiruga/PeriFlakes  
RUN git clone https://github.com/afqueiruga/SimDataDB
/usr/local/lib/pythonlib/SimDataDB  
  
# Define environment variable  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
#ENTRYPOINT ["bash"]  
WORKDIR /home/user  
  
ENTRYPOINT bash --rcfile /opt_cornflakes/source/superbuild/welcome.sh

