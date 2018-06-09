FROM civilmapsdocker/common  
# MAINTAINER Scott Harvey <scott@civilmaps.com>  
# #Python installation  
RUN alias make='make -j4'  
RUN sudo apt-get update && apt-get install -y python-pip wget unzip  
RUN sudo apt-get install -y software-properties-common  
RUN sudo apt-get install -y python-dev  
  
RUN sudo pip install --ignore-install --upgrade cython  
RUN sudo pip install --ignore-install --upgrade numpy  
  
#Python libraries  
RUN sudo apt-get install -y python-matplotlib python-scipy  
  
# Install GEOS for use with shapely  
RUN sudo apt-get install -y libgeos-dev libproj-dev libtiff4-dev libgeotiff-
dev  
  
RUN sudo pip install astropy  
RUN sudo pip install shapely  
RUN sudo pip install --user --install-option="--prefix=" -U scikit-learn  
  
#liblas-laszip  
ADD http://download.osgeo.org/laszip/laszip-2.1.0.tar.gz /home/  
RUN tar xvfz /home/laszip-2.1.0.tar.gz  
RUN mv laszip-2.1.0 /home/  
RUN mkdir /home/laszip-2.1.0/makefiles  
RUN sudo apt-get install -y cmake  
RUN cd /home/laszip-2.1.0/makefiles/ && cmake .. && make && sudo make install  
  
RUN sudo ldconfig  
  
#liblas  
RUN sudo apt-get install -y git  
RUN git clone git://github.com/libLAS/libLAS.git home/liblas  
# RUN sudo apt-get install -y libboost1.55-all-dev  
RUN sudo apt-get install -y libboost-all-dev  
RUN sudo apt-get install -y libgeos-dev libproj-dev libtiff4-dev libgeotiff-
dev  
RUN mkdir home/liblas/makefiles  
ADD https://raw.githubusercontent.com/NLeSC/pointcloud-
benchmark/master/install/centos7/FindPROJ4.cmake home/liblas/cmake/modules/  
RUN cd home/liblas/makefiles/ && cmake -G "Unix Makefiles" .. -DWITH_LASZIP=ON
-DWITH_PKGCONFIG=ON -DWITH_TESTS=ON && make && sudo make install  
# RUN sudo /sbin/ldconfig ##link bindings  
#python bindings for liblas  
RUN sudo pip install liblas  
RUN sudo ldconfig

