FROM ubuntu:14.04.5  
# Install some core software  
RUN apt-get update && apt-get install -y wget g++ make \  
&& rm -rf /var/lib/apt/lists/*  
# Set up the components needed for format support for cdo  
RUN apt-get update && apt-get install -y \  
nco netcdf-bin libhdf5-dev zlib1g-dev libjasper-dev libnetcdf-dev libgrib-api-
dev \  
&& rm -rf /var/lib/apt/lists/*  
# Install cdo from source, so that we get other format support  
WORKDIR /tmp  
RUN wget
https://code.mpimet.mpg.de/attachments/download/16435/cdo-1.9.3.tar.gz -O
/tmp/cdo-1.9.3.tar.gz \  
&& tar -xzvf cdo-1.9.3.tar.gz \  
&& cd /tmp/cdo-1.9.3 \  
&& ./configure --enable-netcdf4 --enable-zlib --with-netcdf=/usr/ \--with-
hdf5=/usr/ \--with-grib_api=/usr/ \  
&& make \  
&& make install \  
&& rm -rf /tmp/*  
  
RUN mkdir -p /data && chmod 777 /data  
WORKDIR /data  
  
CMD cdo --version  

