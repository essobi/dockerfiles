FROM centos:latest  
#Maintainer Todd Wickizer from Bio5 ARL  
  
# Install Orbit tool  
ADD for_redistribution_files_only.zip /root/files.zip  
  
  
# Install basic libraries and x  
RUN yum update -y  
RUN yum install wget unzip libXext libXt-devel libXmu -y  
RUN yum -y install x11vnc firefox xorg-x11-fonts* xorg-x11-xinit
xorg-x11-xinit-session xorg-x11-server-Xvfb xorg-x11-twm tigervnc-server xterm
xorg-x11-font dejavu-sans-fonts dejavu-serif-fonts xdotool; yum clean all  
  
# Install matlab  
RUN mkdir /mcr-install && cd /mcr-install && \  
wget
https://www.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
&& \  
unzip MCR_R2017a_glnxa64_installer.zip && \  
./install -mode silent -agreeToLicense yes  
  
RUN rm -Rf /mcr-install  
  
# set matlab variables  
ENV
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/MATLAB/MATLAB_Runtime/v92/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/java/jre/glnxa64/jre/lib/amd64/server:/usr/local/MATLAB/MATLAB_Runtime/v92/sys/java/jre/glnxa64/jre/lib/amd64  
ENV XAPPLRESDIR=/usr/local/MATLAB/MATLAB_Runtime/v92/X11/app-defaults  
ENV MCR_CACHE_VERBOSE=true  
ENV MCR_CACHE_ROOT=/tmp  
  
RUN mkdir /root/orbit  
RUN unzip -d /root /root/files.zip  
WORKDIR /root/orbit  
ENTRYPOINT ["/root/run_Ex_ReadTDMRotateIOD_FCN.sh",
"/usr/local/MATLAB/MATLAB_Runtime/v92"]  

