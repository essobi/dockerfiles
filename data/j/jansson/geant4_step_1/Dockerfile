FROM jansson/geant4_base  
  
WORKDIR /tmp/geant4/source  
  
# Prevent interactivity.  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y cmake curl  
  
RUN curl -o geant4.${GEANT4_VERSION}.tar.gz \  
http://geant4-data.web.cern.ch/geant4-data/releases/geant4.${GEANT4_VERSION}.tar.gz  
RUN tar -xzf geant4.${GEANT4_VERSION}.tar.gz  
  
WORKDIR /tmp/geant4/build  
  
RUN cmake /tmp/geant4/source/geant4.${GEANT4_VERSION} \  
-DCMAKE_INSTALL_PREFIX=/usr/local/geant4.${GEANT4_VERSION} \  
-DGEANT4_USE_SYSTEM_EXPAT=OFF \  
-DGEANT4_BUILD_MULTITHREADED=ON \  
-DGEANT4_INSTALL_DATA=ON \  
-DGEANT4_USE_OPENGL_X11=ON \  
-DGEANT4_USE_RAYTRACER_X11=ON \  
-DGEANT4_USE_XM=ON  

