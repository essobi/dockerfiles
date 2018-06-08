#################################################################  
# Dockerfile  
#  
# Version: 1.0  
# Software: OptiType  
# Software Version: 1.3  
# Description: Accurate NGS-based 4-digit HLA typing  
# Modified from https://github.com/FRED-2/OptiType  
# for the use with nextflow.  
# Modifications: removed USER biodocker  
# removed entry point  
# changed command to CMD ["/bin/bash"]  
# Added bedtools  
# Using slightly modified version of OptiType prints to stdout  
#################################################################  
  
# Source Image  
FROM biocontainers/biocontainers:latest  
  
################## BEGIN INSTALLATION ###########################  
USER root  
  
# install  
RUN apt-get update && apt-get install -y software-properties-common \  
&& apt-get update && apt-get install -y \  
gcc-4.9 \  
g++-4.9 \  
coinor-cbc \  
zlib1g-dev \  
libbz2-dev \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 \--slave
/usr/bin/g++ g++ /usr/bin/g++-4.9 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& apt-get purge  
  
#HLA Typing  
#OptiType dependecies  
RUN curl -O https://support.hdfgroup.org/ftp/HDF5/current18/bin/linux-
centos7-x86_64-gcc485/hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared.tar.gz \  
&& tar -xvf hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared.tar.gz \  
&& mv hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared/bin/* /usr/local/bin/ \  
&& mv hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared/lib/* /usr/local/lib/ \  
&& mv hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared/include/*
/usr/local/include/ \  
&& mv hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared/share/* /usr/local/share/
\  
&& rm -rf hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared/ \  
&& rm -f hdf5-1.8.19-linux-centos7-x86_64-gcc485-shared.tar.gz  
  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
ENV HDF5_DIR /usr/local/  
ENV PATH=/usr/local/bin/OptiType:$PATH  
ENV PATH=/opt/conda/bin:$PATH  
  
RUN pip install --upgrade pip && pip install \  
numpy \  
pyomo \  
pysam \  
matplotlib \  
tables \  
pandas \  
future  
  
#installing optitype form git repository (version Dec 09 2015) and wirtig
config.ini  
RUN git clone -b add-ID https://git@github.com/mhalagan-nmdp/OptiType.git \  
&& sed -i -e '1i#!/usr/bin/env python\' OptiType/OptiTypePipeline.py \  
&& mv OptiType/ /usr/local/bin/ \  
&& chmod 777 /usr/local/bin/OptiType/OptiTypePipeline.py \  
&& echo "[mapping]\n\  
razers3=/usr/local/bin/razers3 \n\  
threads=1 \n\  
\n\  
[ilp]\n\  
solver=cbc \n\  
threads=1 \n\  
\n\  
[behavior]\n\  
deletebam=true \n\  
unpaired_weight=0 \n\  
use_discordant=false\n" >> /usr/local/bin/OptiType/config.ini  
#installing razers3  
RUN git clone https://github.com/seqan/seqan.git seqan-src \  
&& cd seqan-src \  
&& cmake -DCMAKE_BUILD_TYPE=Release \  
&& make razers3 \  
&& cp bin/razers3 /usr/local/bin \  
&& cd .. \  
&& rm -rf seqan-src  
  
RUN conda install samtools -y  
  
# Change user to back to biodocker  
RUN wget
https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
\  
&& tar -zxvf bedtools-2.25.0.tar.gz \  
&& cd bedtools2 && make \  
&& mv bin/* /usr/local/bin/  
  
# Change workdir to /data/  
WORKDIR /data/  
# Define default command  
CMD ["/bin/bash"]  
##################### INSTALLATION END ##########################  
# File Author / Maintainer  
MAINTAINER Michael Halagan <mhalagan@nmdp.org>  

