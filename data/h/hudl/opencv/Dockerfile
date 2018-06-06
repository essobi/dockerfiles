FROM hudl/ffmpeg  
  
MAINTAINER Ryan Versaw <ryan.versaw@hudl.com>  
  
# Dependencies  
RUN apt-get update && apt-get install -y \  
cmake \  
gfortran \  
libatlas-base-dev \  
python \  
python-dev \  
wget  
  
# Download OpenCV and extra modules  
WORKDIR /  
RUN git clone https://github.com/Itseez/opencv.git  
WORKDIR /opencv  
RUN git checkout tags/3.1.0  
  
WORKDIR /  
RUN git clone https://github.com/Itseez/opencv_contrib.git  
WORKDIR /opencv_contrib  
RUN git checkout tags/3.1.0  
  
# Build OpenCV  
WORKDIR /opencv  
RUN cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules . && \  
make && make install && \  
ldconfig && \  
cd .. && \  
rm -rf opencv && \  
rm -rf opencv_contrib  
  
WORKDIR /  
RUN curl -L ftp://ftp.gnu.org/gnu/gsl/gsl-2.1.tar.gz | tar zxf - && \  
cd gsl-2.1 && \  
./configure && \  
make && make install && \  
ldconfig && \  
cd .. && \  
rm -rf gsl-2.1  
  
# Install Boost  
RUN apt-get update  
RUN apt-get install -y libboost-all-dev --fix-missing  
ENV LC_ALL=C  
  
# Install VLFeat  
RUN wget http://www.vlfeat.org/download/vlfeat-0.9.20-bin.tar.gz  
RUN tar zxvf vlfeat-0.9.20-bin.tar.gz  
RUN rm vlfeat-0.9.20-bin.tar.gz  
ENV VLFEAT_DIR=/vlfeat-0.9.20  
# Install Eigen3  
RUN apt-get install -y libeigen3-dev  
  
# Install HDF5  
RUN apt-get install -y libhdf5-serial-dev --fix-missing  
  
# Install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py && rm get-pip.py  
RUN pip install --upgrade pip  
  
# Python stack  
COPY ./requirements.txt /root/  
RUN pip install -r /root/requirements.txt  
RUN rm /root/requirements.txt  
  

