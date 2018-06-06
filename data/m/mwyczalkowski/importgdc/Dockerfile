FROM ubuntu:latest  
  
LABEL author="Matt Wyczalkowski" \  
maintainer="m.wyczalkowski@wustl.edu"  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
jq \  
libnss-sss \  
trickle \  
samtools \  
vim \  
wget \  
zip \  
&& apt-get clean  
  
RUN cd /usr/local \  
&& wget https://gdc.cancer.gov/system/files/authenticated%20user/0/gdc-
client_v1.3.0_Ubuntu14.04_x64.zip \  
&& unzip gdc-client_v1.3.0_Ubuntu14.04_x64.zip \  
&& mv gdc-client /usr/local/bin  
  
RUN cd /usr/local \  
&& git clone https://github.com/ding-lab/importGDC.git  
  
CMD ["/bin/bash"]  

