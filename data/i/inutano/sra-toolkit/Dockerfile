# Docker container for SRAToolKit developed by NCBI Genbank/SRA team.  
# Pull base image.  
FROM ubuntu:14.04.4  
# :)  
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com  
  
# clone repo  
WORKDIR /src  
ENV VERSION 2.9.0  
RUN apt-get update -y && apt-get install -y wget git  
  
# Install sra-toolkit  
RUN wget "http://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/${VERSION}/sratoolkit.${VERSION}-ubuntu64.tar.gz"
&& \  
tar zxfv sratoolkit.${VERSION}-ubuntu64.tar.gz && \  
cp -r sratoolkit.${VERSION}-ubuntu64/bin/* /usr/bin  
  
# Install pfastq-dump  
RUN git clone https://github.com/inutano/pfastq-dump && \  
cd pfastq-dump && \  
chmod a+x bin/pfastq-dump && \  
cp bin/pfastq-dump /usr/bin  
  
# Default command  
WORKDIR /data  
CMD ["bash"]  

