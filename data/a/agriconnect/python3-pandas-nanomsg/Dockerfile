FROM debian:buster  
MAINTAINER Nguyễn Hồng Quân <ng.hong.quan@gmail.com>  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python3-dev python3-pip cython3 \  
liblapack-dev libatlas-base-dev gfortran \  
libfreetype6-dev libpng-dev libjpeg-dev libpq-dev \  
cmake wget git && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# Install nanomsg  
RUN wget -qO- https://github.com/nanomsg/nanomsg/archive/1.0.0.tar.gz | tar xz
&& \  
cd nanomsg-1.0.0 && mkdir build && cd build && \  
cmake .. && cmake --build . && cmake --build . --target install && ldconfig &&
\  
cd ../.. && rm -rf nanomsg-1.0.0  
# Install Python3 libs. Numpy should be explicitly installed before Pandas, or
pandas will make numpy built twice.  
RUN pip3 install -U pip && pip3 install numpy && pip3 install pandas  

