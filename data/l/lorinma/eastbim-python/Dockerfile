from phusion/baseimage:0.9.16  
MAINTAINER lorinma <malingreal [at] gmail {dot} com>  
  
run apt-get update -y; \  
apt-get install -y --force-yes --no-install-recommends curl git build-
essential cmake cmake-curses-gui \  
python-software-properties software-properties-common subversion libboost-all-
dev vim \  
unzip tree mesa-common-dev freeglut3-dev freetype* SWIG python-pip  
  
# compile occ  
run cd /usr/local/src/; git clone https://github.com/tpaviot/oce.git; cd oce;
git checkout OCE-0.16; mkdir build; \  
cd build; cmake ../; make -j4; make install/strip; cd ../../; rm -rf oce  
  
# compile python-occ  
run cd /usr/local/src/; git clone https://github.com/tpaviot/pythonocc-
core.git; cd pythonocc-core; \  
git checkout 0.16.0; mkdir build; cd build; cmake ..; make -j4; make install;
cd ../../; rm -rf pythonocc-core  
  
#compile ifcopenshell from source, seems the latest ifcopenshell only support  
#oce 0.16.0  
#RUN cd /usr/local/src/ && svn checkout
svn://svn.code.sf.net/p/ifcopenshell/svn/tags/0.5.0-preview1/ ifcopenshell &&
mkdir ifcopenshell/cmake/build && cd ifcopenshell/cmake/build && cmake
-DOCC_INCLUDE_DIR:STRING=/usr/include/oce .. && make -j4 && make install  
#install the ifcopenshell-python package to python packages directory  
ENV DEV /usr/local/lib/python2.7/dist-packages  
ADD https://github.com/lorinma/eastbim-
python/releases/download/test/ifcopenshell-
python-2.7-0.5.0-preview1-linux64.zip $DEV.zip  
RUN unzip $DEV.zip -d $DEV; rm $DEV.zip  
  
# RUN pip install -r requirements.txt  
RUN pip install Flask-PyMongo numpy validate_email  
  
# ADD . /web  
# WORKDIR /web  
# # clone this git repository  
# run cd /; git clone https://github.com/lorinma/eastbim-python.git web  

