# Docker image for SRA_Toolkit  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# install  
RUN apt-get update && apt-get install -y \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install SRA_toolkit  
WORKDIR /src  
ENV VERSION 2.8.2-1  
RUN wget "https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/${VERSION}/sratoolkit.${VERSION}-ubuntu64.tar.gz"
\  
&& tar zxvf sratoolkit.${VERSION}-ubuntu64.tar.gz \  
&& rm -rf sratoolkit.${VERSION}-ubuntu64.tar.gz \  
&& ln -s /src/sratoolkit.2.8.2-1-ubuntu64/bin/* /usr/bin  
  
# initialize  
WORKDIR /mount  
CMD ["bash"]  

