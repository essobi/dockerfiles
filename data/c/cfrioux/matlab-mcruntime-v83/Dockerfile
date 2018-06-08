# Base for matlab-runtime-v83  
#  
# VERSION 0.1  
#  
# build : docker build -t image_name .  
# usage: docker run -ti -v /path/to/share:/mount/point image_name bash  
#  
FROM java:openjdk-8u72-jre  
MAINTAINER clemence.frioux@gmail.com  
  
RUN apt-get update && \  
apt-get install -y curl wget unzip xorg  
# Install MatLab runtime  
RUN \  
mkdir /root/mosek && chmod 777 /root/mosek && \  
mkdir /mcr-install && \  
cd /mcr-install && \  
wget -nv
http://fr.mathworks.com/supportfiles/downloads/R2014a/deployment_files/R2014a/installers/glnxa64/MCR_R2014a_glnxa64_installer.zip
&& \  
unzip MCR_R2014a_glnxa64_installer.zip && \  
mkdir /opt/mcr && \  
./install -mode silent -agreeToLicense yes && \  
cd / && \  
rm -rf mcr-install  
  
RUN touch /tmp/mosek.lic && ln -s /tmp/mosek.lic /root/mosek/mosek.lic  
  
#mcr is here /usr/local/MATLAB/MATLAB_Compiler_Runtime/v83/  
#put the mosek license file in /root/mosek  

