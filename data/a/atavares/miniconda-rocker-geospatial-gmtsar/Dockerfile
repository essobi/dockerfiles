  
FROM atavares/miniconda-rocker-geospatial:latest  
  
RUN apt-get update --fix-missing && apt-get install -y csh subversion autoconf
libtiff5-dev libhdf5-dev \  
liblapack-dev \  
gfortran \  
g++ \  
libgmt-dev \  
gmt  
  
RUN mkdir /usr/local/orbits  
  
RUN wget http://topex.ucsd.edu/gmtsar/tar/ORBITS.tar -P /usr/local/orbits  
  
RUN tar -xvf /usr/local/orbits/ORBITS.tar -C /usr/local/orbits/  
  
RUN svn checkout svn://gmtserver.soest.hawaii.edu/GMTSAR/branches/5.4
/usr/local/GMTSAR  
  
RUN cd /usr/local/GMTSAR \  
&& autoconf \  
&& ./configure --with-orbits-dir=/usr/local/orbits \  
&& make \  
&& make install  
  
ENV GMTSAR="/usr/local/GMTSAR"  
ENV PATH="${GMTSAR}/bin:${PATH}"  
## Download a two-pass processing sample dataset:  
#ENV GMTSAR_DATASET="ALOS_Baja_EQ"  
#  
#RUN wget -q ftp://topex.ucsd.edu/pub/gmtsar/${GMTSAR_DATASET}.tar.gz \  
# && mkdir ${GMTSAR_DATASET} \  
# && cd ${GMTSAR_DATASET} \  
# && tar xzvf ../${GMTSAR_DATASET}.tar.gz \  
# && cd .. \  
# && rm ${GMTSAR_DATASET}.tar.gz  

