# Docker image for Bowtie2  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update && apt-get install -y \  
wget \  
unzip \  
gzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Bowtie2  
WORKDIR /src  
RUN wget https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-linux-x86_64.zip \  
&& unzip bowtie2-2.3.3.1-linux-x86_64.zip \  
&& rm -rf bowtie2-2.3.3.1-linux-x86_64.zip \  
&& ln -s /src/bowtie2-2.3.3.1-linux-x86_64/bowtie2 /usr/local/bin/ \  
&& ln -s /src/bowtie2-2.3.3.1-linux-x86_64/bowtie2-build /usr/local/bin/ \  
&& ln -s /src/bowtie2-2.3.3.1-linux-x86_64/bowtie2-inspect /usr/local/bin/  
  
WORKDIR /mount  
CMD ["bash"]  

