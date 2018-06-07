FROM ubuntu:16.04  
# clean up cache  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
RUN apt-get update -o Acquire::CompressionTypes::Order::=gz  
  
# install packages  
RUN apt-get install python -y  
RUN apt-get install python-pip -y  
RUN apt-get install libhdf5-serial-dev -y  
RUN apt-get install wget -y  
RUN apt-get install subversion -y  
RUN apt-get install nco -y  
RUN apt-get install ffmpeg -y  
  
# install build dependencies  
RUN apt-get build-dep python-matplotlib -y  
  
# build hdf5 and netcdf  
RUN wget http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.17.tar.gz  
RUN tar -xvf hdf5-1.8.17.tar.gz  
RUN cd hdf5-1.8.17 && ./configure --prefix=/usr/local \--enable-shared
--enable-hl && make && make install  
RUN cd ..  
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.1.3.tar.gz  
RUN tar -xvf netcdf-4.1.3.tar.gz  
RUN cd netcdf-4.1.3 && ./configure && make && make install  
  
# install pip packages  
RUN mkdir -m 775 /data  
ADD requirements.txt /data/requirements.txt  
RUN pip install -r /data/requirements.txt  
  
# set matplotlib backend to Agg  
RUN mkdir -p /root/.config/matplotlib  
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc  

