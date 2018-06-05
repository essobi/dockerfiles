FROM ubuntu  
  
MAINTAINER Frederic Lemoine  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y unzip python wget g++ gcc make bzip2 libncurses5-dev
zlib1g-dev  
  
RUN \  
wget "http://downloads.sourceforge.net/project/bowtie-
bio/bowtie2/2.2.8/bowtie2-2.2.8-linux-x86_64.zip?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fbowtie-
bio%2Ffiles%2Fbowtie2%2F2.2.8%2F&ts=1461156134&use_mirror=ufpr" && \  
mv bowtie2-2.2.* bowtie2-2.2.8-linux-x86_64.zip && \  
unzip bowtie2-2.2.8-linux-x86_64.zip && \  
mkdir /opt/bowtie2/ && \  
cp bowtie2-2.2.8/bowtie2* /opt/bowtie2 && \  
rm -rf bowtie2-2.2.8/ bowtie2-2.2.8-linux-x86_64.zip  
  
RUN \  
wget
http://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
\  
&& tar -xjvf samtools-1.3.1.tar.bz2 \  
&& cd samtools-1.3.1 \  
&& ./configure \  
&& make \  
&& mkdir /opt/samtools/ \  
&& mv samtools /opt/samtools/ \  
&& cd .. \  
&& rm -rf samtools-1.3.1 samtools-1.3.1.tar.bz2  
  
#  
# Finalize environment  
#  
RUN apt-get remove -q -y zlib1g-dev libncurses5-dev wget g++ gcc make bzip2
unzip wget \  
&& apt-get autoremove -y  
  
ENV PATH
/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/bowtie2:/opt/samtools  

