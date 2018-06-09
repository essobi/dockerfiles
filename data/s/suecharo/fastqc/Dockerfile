# Docker image for Trinity  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk \  
wget \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install FastQC  
WORKDIR /src  
RUN wget
https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip \  
&& unzip fastqc_v0.11.5.zip \  
&& rm -rf fastqc_v0.11.5.zip \  
&& chmod 755 /src/FastQC/fastqc \  
&& ln -s /src/FastQC/fastqc /usr/local/bin/  
  
WORKDIR /mount  
CMD ["bash"]  

