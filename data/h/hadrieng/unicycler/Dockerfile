FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install python3  
RUN apt-get install -y python3 python3-pkg-resources python3-pip  
  
# install samtools deps  
RUN apt-get install -y libbz2-dev liblzma-dev  
  
# install minimap2  
RUN git clone https://github.com/lh3/minimap2 && \  
cd minimap2 && \  
make && \  
cd ..  
  
# cmake 3.2  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz && \  
tar xf cmake-3.2.2.tar.gz && \  
cd cmake-3.2.2 && \  
./configure && \  
make && \  
make install  
  
# install racon  
RUN git clone \--recursive https://github.com/isovic/racon.git && \  
cd racon && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=Release .. && \  
make  
  
# install java-1.8  
RUN echo 'deb http://ftp.de.debian.org/debian jessie-backports main' \  
>> /etc/apt/sources.list && \  
apt-get update --fix-missing && \  
apt install -y -t jessie-backports \  
openjdk-8-jre-headless \  
ca-certificates-java \  
openjdk-8-jdk && \  
/usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
# install pilon  
RUN latest=$(curl https://api.github.com/repos/broadinstitute/pilon/releases |
grep browser_download_url | grep '.jar' | head -n 1 | cut -d '"' -f 4) && \  
wget $latest && \  
cp pilon-?.??.jar /usr/bin/ && \  
echo -e '#!/bin/bash\njava -jar /pilon-?.??.jar $@' > /usr/bin/pilon  
  
# install samtools  
RUN latest=$(curl -s https://api.github.com/repos/samtools/samtools/releases |
grep browser_download_url | grep 'tar.bz2' | head -n 1 | cut -d '"' -f 4) && \  
wget $latest && \  
tar xjf samtools-?.?.tar.bz2 && \  
cd samtools-?.? && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf samtools-?.*  
  
# install bowtie2  
RUN latest=$(curl -s https://api.github.com/repos/BenLangmead/bowtie2/releases
| grep browser_download_url | grep 'linux-x86_64.zip' | head -n 1 | cut -d '"'
-f 4) && \  
wget $latest && \  
unzip bowtie2-?.*-linux-x86_64.zip && \  
mv bowtie2-?.*-linux-x86_64 bowtie2 && \  
rm bowtie2-?.*-linux-x86_64.zip  
  
# install spades  
RUN latest=$(curl -s https://api.github.com/repos/ablab/spades/releases | grep
browser_download_url | grep 'Linux.tar.gz' | head -n 1 | cut -d '"' -f 4) && \  
wget $latest && \  
tar xzf SPAdes-?.*-Linux.tar.gz && \  
mv SPAdes-?.*-Linux spades && \  
rm SPAdes-?.*-Linux.tar.gz  
  
# install blast  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-
blast-?.?.?+-x64-linux.tar.gz && \  
tar xzf ncbi-blast-?.?.?+-x64-linux.tar.gz && \  
mv ncbi-blast-?.?.?+ blast && \  
rm ncbi-blast-?.?.?+-x64-linux.tar.gz  
  
# install unicycler  
RUN pip3 install git+https://github.com/rrwick/Unicycler.git  
  
ENV PATH /minimap2:/racon/build/bin:/bowtie2:/spades/bin:/blast/bin:$PATH  

