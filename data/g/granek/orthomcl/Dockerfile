FROM debian:jessie-backports  
  
#----------------------------  
# Install debian dependencies  
#----------------------------  
RUN apt-get update && \  
apt-get -t jessie-backports install -y --no-install-recommends \  
ca-certificates \  
g++ \  
less \  
libdbd-mysql-perl \  
libdbi-perl \  
make \  
mysql-client \  
perl \  
tar \  
wget \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Make a software folder  
RUN mkdir /software  
  
#--------------  
# Install blast  
#--------------  
RUN cd /software \  
&& wget
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/legacy/2.2.26/blast-2.2.26-x64-linux.tar.gz
\  
&& tar -xzvf blast-2.2.26-x64-linux.tar.gz \  
&& rm blast-2.2.26-x64-linux.tar.gz  
  
#--------------  
# Install MCL  
#--------------  
RUN cd /software \  
&& wget http://micans.org/mcl/src/mcl-14-137.tar.gz \  
&& tar -xzvf mcl-14-137.tar.gz \  
&& rm mcl-14-137.tar.gz \  
&& cd /software/mcl-14-137 \  
&& ./configure --enable-blast --prefix=/software/mcl \  
&& make install \  
&& cd /software \  
&& rm -rf /software/mcl-14-137  
#-----------------  
# Install OrthoMCL  
#-----------------  
RUN cd /software \  
&& wget
http://www.orthomcl.org/common/downloads/software/v2.0/orthomclSoftware-v2.0.9.tar.gz
\  
&& tar -xzvf orthomclSoftware-v2.0.9.tar.gz \  
&& rm orthomclSoftware-v2.0.9.tar.gz  
  
#----------------  
# Setup the paths  
#----------------  
ENV PATH $PATH:/software/blast-2.2.26/bin  
ENV PATH $PATH:/software/mcl/bin  
ENV PATH $PATH:/software/orthomclSoftware-v2.0.9/bin  
  
#------------------  
# Add config script  
#------------------  
ADD test_run/create_config.sh /software/create_config.sh  

