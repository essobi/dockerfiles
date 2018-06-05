#####################################################3  
# shot out to  
# matt.mccormick@kitware.com for the example of VTK build in docker  
# https://github.com/KitwareMedical/docker-pluslib/blob/master/Dockerfile  
#  
# latest Ubuntu  
FROM ubuntu:15.10  
MAINTAINER gbivins "gbivins4@gmail.com"  
RUN apt-get update  
  
#java 8  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get install oracle-java8-set-default  
  
ENV TMP_SRC_DIR /tmp/src  
ENV VTK_LIBS=/opt/bin/VTK/lib  
ENV VTK_JAR=${VTK_LIBS}/vtk.jar  
  
RUN mkdir ${TMP_SRC_DIR}  
RUN mkdir -p ${VTK_LIBS}  
  
ADD ./vtk.jar ${VTK_LIBS}/vtk.jar  
ADD ./vtk-natives-Linux-x86_64.jar ${VTK_LIBS}/vtk-natives-Linux-x86_64.jar  
WORKDIR ${VTK_LIBS}  
RUN jar xvf ${VTK_LIBS}/vtk-natives-Linux-x86_64.jar  
RUN rm -rf ${VTK_LIBS}/cmake  
  
WORKDIR ${TMP_SRC_DIR}  
ADD ./TestVTKInstall.java ${TMP_SRC_DIR}/TestVTKInstall.java  
ENV LD_LIBRARY_PATH=${VTK_LIBS}:${LD_LIBRARY_PATH}  
  
RUN javac -version -classpath ${VTK_JAR} TestVTKInstall.java  
#CMD java -Dvtk.lib.dir=${VTK_LIBS} -cp ${VTK_JAR}:. TestVTKInstall  
CMD java -cp ${VTK_JAR}:. TestVTKInstall  
  

