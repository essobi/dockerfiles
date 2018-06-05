FROM rocker/geospatial:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
libxml2-dev \  
libcurl4-openssl-dev \  
libboost-dev \  
gfortran  
  
ENV CC gcc  
  
ENV FC gfortran  
  
# ref: https://bovineaerospace.wordpress.com/2014/01/24/how-to-install-
rnomads-on-linux/  
  
RUN curl -O http://www.ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz && \  
sudo tar -xvf wgrib2.tgz && \  
cd grib2/ && \  
make && \  
sudo mv wgrib2/ /usr/local && \  
cd .. && \  
sudo mkdir wgrib && \  
curl -O ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/wgrib.tar && \  
sudo mv wgrib.tar wgrib && \  
cd wgrib && \  
sudo tar -xvf wgrib.tar && \  
make && \  
sudo mkdir /usr/local/wgrib && \  
sudo mv * /usr/local/wgrib  
  
ENV PATH /usr/local/wgrib2:/usr/local/wgrib:${PATH}  
  
RUN install2.r --error \  
GEOmap \  
rNOMADS \  
selectr  
  
  

