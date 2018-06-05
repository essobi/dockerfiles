FROM tiangolo/uwsgi-nginx-flask:flask  
  
RUN apt update -y && \  
apt install wget unzip libxext6 libxext-dev libxmu6 -y && \  
mkdir /mcr-install && \  
mkdir /opt/mcr && \  
cd /mcr-install && \  
wget -nv
http://www.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
&& \  
unzip MCR_R2017a_glnxa64_installer.zip && \  
./install -destinationFolder /opt/mcr -mode silent -agreeToLicense yes && \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/mcr/v92/runtime/glnxa64:/opt/mcr/v92/bin/glnxa64:/opt/mcr/v92/sys/os/glnxa64
&& \  
rm -Rf /mcr-install && \  
cd /opt/mcr/v92/toolbox/compiler_sdk/pysdk_py && \  
python setup.py install  

