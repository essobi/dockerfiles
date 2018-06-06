# FROM glatard/matlab-compiler-runtime-docker:latest  
# Originally used glatard's Matlab docker, however  
# that is build on R2016a and project needs R2016b.  
# Replacing link in Glatard's script.  
from centos:latest  
RUN yum update -y  
RUN yum install wget unzip libXext libXt-devel libXmu -y  
RUN mkdir /mcr-install && cd /mcr-install && \  
wget -nv
http://www.mathworks.com/supportfiles/downloads/R2016b/deployment_files/R2016b/installers/glnxa64/MCR_R2016b_glnxa64_installer.zip
&& \  
unzip MCR_R2016b_glnxa64_installer.zip && \  
./install -mode silent -agreeToLicense yes  
RUN rm -Rf /mcr-install  
ENV
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/MATLAB/MATLAB_Runtime/v91/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v91/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v91/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v91/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:/usr/local/MATLAB/MATLAB_Runtime/v91/sys/java/jre/glnxa64/jre/lib/amd64/server:/usr/local/MATLAB/MATLAB_Runtime/v91/sys/java/jre/glnxa64/jre/lib/amd64  
ENV XAPPLRESDIR=/usr/local/MATLAB/MATLAB_Runtime/v91/X11/app-defaults  
ENV MCR_CACHE_VERBOSE=true  
ENV MCR_CACHE_ROOT=/tmp  
  
# End modification of Glatard's script.  
RUN yum reinstall ca-certificates -y  
RUN yum install git perl-ExtUtils-Embed gcc* make zlib-devel -y  
RUN git config --global http.sslverify "false"  
RUN git clone http://github.com/cooperative-computing-lab/cctools
$HOME/cctools-src \  
&& cd $HOME/cctools-src \  
&& bash ./configure --prefix $HOME/cctools \  
&& make && make install && rm -rf $HOME/cctools-src && cd $HOME  
# Hardcoded /root path as $HOME was not replacing in PATH correctly  
ENV PATH=/root/cctools/bin:$PATH  

