FROM ubuntu:xenial  
ARG DEBIAN_FRONTEND=noninteractive  
LABEL maintainer "Trevor SANDY <trevor.sandy@gmail.com>"  
RUN apt-get update ; apt-get install -y apt-utils git wget lintian build-
essential debhelper fakeroot ccache lsb-release  
RUN apt-get install -y qtbase5-dev qt5-qmake libqt5opengl5-dev libpng-dev
libjpeg-dev zlib1g-dev  
RUN apt-get install -y libboost-thread1.58.0 libtiff5 libosmesa6 freeglut3  
VOLUME /buildpkg  
CMD wget
https://raw.githubusercontent.com/trevorsandy/lpub3d-ci/master/builds/linux/CreateDeb.sh
\  
&& chmod +x CreateDeb.sh \  
&& ./CreateDeb.sh \  
&& if test -d /buildpkg; then cp -f /debbuild/*.deb /buildpkg/; fi  

