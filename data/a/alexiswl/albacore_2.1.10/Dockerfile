### BASE IMAGE ###  
FROM ubuntu:trusty  
  
### METADATA ###  
LABEL base.image="ubuntu:trusty"  
LABEL docker.version="1"  
LABEL software="albacore"  
LABEL software.version="2.1.10"  
LABEL description="Albacore is a program for basecalling nanopore fast5 files"  
LABEL website="nanoporetech.com"  
  
### MAINTAINER ###  
MAINTAINER Alexis Lucattini <alexis.lucattini@agrf.org.au>  
  
### INSTALLATION ###  
# Install wget and https  
RUN apt-get update  
RUN apt-get install -y wget apt-transport-https  
  
# Add nanopore repo  
RUN wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | apt-key
add -  
RUN echo "deb http://mirror.oxfordnanoportal.com/apt trusty-stable non-free" |
\  
sudo tee /etc/apt/sources.list.d/nanoporetech.sources.list  
RUN apt-get update  
RUN apt-cache policy python3-ont-albacore  
  
# Install dependencies  
RUN apt-get install -y libboost-filesystem1.54.0 \  
libboost-program-options1.54.0 \  
libhdf5.7 \  
libboost-python1.54.0 \  
python3-h5py \  
python3-numpy \  
python3-dateutil \  
python3-ont-fast5-api \  
python3-progressbar \  
python3-setuptools  
  
# Install the debian  
RUN TEMP_DEB="$(mktemp)" && \  
wget -O "$TEMP_DEB"
https://mirror.oxfordnanoportal.com/software/analysis/python3-ont-
albacore_2.1.10-1~trusty_amd64.deb && \  
dpkg -i "$TEMP_DEB" && \  
rm -f "$TEMP_DEB"  
  
# Reset apt  
RUN sudo apt-get -f install  
  
WORKDIR /data  
  
# Run the albacore command from entry point  
ENTRYPOINT ['read_fast5_basecaller.py']  

