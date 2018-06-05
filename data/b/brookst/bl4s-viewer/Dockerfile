FROM fedora:latest  
  
MAINTAINER Tim Brooks <brooks@cern.ch>  
  
#Install required system packages  
RUN yum install -y tar unzip glibc.i686 libgcc libgcc.i686 libXinerama.i686
mesa-libGL.i686  
  
#Create a user  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/ni && \  
echo "ni:x:${uid}:${gid}:NI,,,:/home/ni:/bin/bash" >> /etc/passwd && \  
echo "ni:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/ni  
  
#Install the Labview Run-Time Engine  
RUN mkdir -p /home/ni/rte  
WORKDIR /home/ni/rte  
RUN curl -O
http://download.ni.com/support/softlib/labview/labview_runtime/2013%20SP1/Linux/LabVIEW2013SP1RTE_Linux.tgz
&& \  
tar -xzf LabVIEW2013SP1RTE_Linux.tgz && \  
rpm -Uvh *.rpm  
  
#Clean up installation files  
WORKDIR /home/ni  
RUN rm -rf /home/ni/rte  
  
#Install the Beamline for Schools viewer application  
RUN mkdir -p /home/ni/bl4s  
WORKDIR /home/ni/bl4s  
RUN curl -O
ftp://ftp.ni.com/pub/branches/ee/BLS4/BL4SEventViewerLinuxBinary.zip && \  
unzip BL4SEventViewerLinuxBinary.zip && \  
chmod +x BL4SEventViewerLinuxBinary/BL4SApp  
  
#Configure runtime  
USER ni  
ENV HOME /home/ni  
CMD /home/ni/bl4s/BL4SEventViewerLinuxBinary/BL4SApp  

