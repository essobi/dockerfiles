FROM nimbix/ubuntu-desktop:trusty  
MAINTAINER stephen.fox@nimbix.net  
  
RUN apt-get update && apt-get install -y curl  
RUN mkdir -p /usr/local/src  
  
WORKDIR /usr/local/src  
RUN curl -O "http://www.paraview.org/paraview-
downloads/download.php?submit=Download&version=v5.1&type=binary&os=linux64&downloadFile=ParaView-5.1.2-Qt4-OpenGL2-MPI-
Linux-64bit.tar.gz"  
RUN tar xvf
"download.php?submit=Download&version=v5.1&type=binary&os=linux64&downloadFile=ParaView-5.1.2-Qt4-OpenGL2-MPI-
Linux-64bit.tar.gz"  
  
RUN mv /usr/local/src/ParaView-5.1.2-Qt4-OpenGL2-MPI-Linux-64bit
/usr/local/ParaView-5.1.2  
RUN rm
"/usr/local/src/download.php?submit=Download&version=v5.1&type=binary&os=linux64&downloadFile=ParaView-5.1.2-Qt4-OpenGL2-MPI-
Linux-64bit.tar.gz"  
  
ADD ./scripts /usr/local/scripts  
  
# Add PushToCompute Work Flow Metadata  
ADD ./NAE/nvidia.cfg /etc/NAE/nvidia.cfg  
ADD ./NAE/AppDef.png /etc/NAE/AppDef.png  
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json  
COPY ./NAE/screenshot.png /etc/NAE/screenshot.png  
  
CMD /usr/local/scripts/start.sh  

