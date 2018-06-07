#####################################################3  
# shot out to  
# matt.mccormick@kitware.com for the example of VTK build in docker  
# https://github.com/KitwareMedical/docker-pluslib/blob/master/Dockerfile  
# jess@docker.com for the glxgears example which showed how to run without
installing  
# X11 in the container  
#  
# Make sure you do an "xhost +" before running  
# run with something like this:  
# sudo docker run  
# -v=/tmp/.X11-unix:/tmp/.X11-unix  
# --privileged  
# -e DISPLAY=unix$DISPLAY  
# --device /dev/ati  
# vtk-examples bin/<name of example to run> //like vtk bin/Cone  
#  
#  
#  
FROM gbivins/vtk-base-java:v6.3.0.rc2  
MAINTAINER gbivins "gbivins4@gmail.com"  
RUN apt-get update  
  
RUN apt-get install -y wget  
RUN apt-get install -y build-essential  
RUN apt-get install -y cmake cmake-curses-gui  
RUN apt-get install -y ninja-build  
  
RUN mkdir -p /opt/{src,bin}  
WORKDIR /opt/src  
  
## examples  
RUN mkdir -p /opt/src/VTKExamples  
WORKDIR /opt/src/VTKExamples  
  
RUN echo "re-getting archive" && wget
https://github.com/lorensen/VTKWikiExamples/archive/master.zip  
RUN unzip master.zip  
  
#Remove testing from all the CMake Files so that builds don't fail  
RUN mv VTKWikiExamples-master/Cxx/Visualization/StreamLines.cxx
VTKWikiExamples-master/Cxx/Visualization/StreamLines.cxx.bak  
  
RUN mkdir -p /opt/bin/VTKExamples  
WORKDIR /opt/bin/VTKExamples  
RUN cmake -G Ninja \  
-DCMAKE_BUILD_TYPE:STRING=Release \  
-DBUILD_TESTING:BOOL=OFF \  
-DCMAKE_INSTALL_PREFIX:PATH=/.../install \  
-DVTK_WRAP_JAVA:BOOL=ON \  
-DVTK_DIR:PATH=/opt/bin/VTK \  
../../src/VTKExamples/VTKWikiExamples-master  
RUN ninja  
  
CMD ls  
  

