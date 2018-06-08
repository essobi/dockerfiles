FROM thewtex/centos-build:v1.0.0  
MAINTAINER SlicerProstate http://github.com/SlicerProstate  
  
RUN yum update -y  
  
WORKDIR /usr/src  
  
RUN git clone https://github.com/fedorov/InsightToolkit-3.20.1.git && mkdir
/usr/src/ITK-build && cd /usr/src/ITK-build && cmake -DBUILD_EXAMPLES=OFF
-DBUILD_TESTING=OFF -DBUILD_TYPE=Release -DITK_USE_REVIEW=ON
-DUSE_REVIEW_STATISTICS=ON /usr/src/InsightToolkit-3.20.1
../InsightToolkit-3.20.1 && make  
  
RUN git clone https://github.com/fedorov/ProstateRegistrationITKv3.git &&
mkdir Registration-build && cd Registration-build && cmake
-DITK_DIR=/usr/src/ITK-build ../ProstateRegistrationITKv3 && make  

