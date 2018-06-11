FROM ubuntu:xenial  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
description="Image for tools used in RnaSeq"  
  
RUN apt-get update -y && apt-get install -y \  
build-essential \  
bzip2 \  
cmake \  
default-jdk \  
git \  
libnss-sss \  
libtbb2 \  
libtbb-dev \  
nodejs \  
python-dev \  
python-pip \  
tzdata \  
unzip \  
wget \  
zlib1g \  
zlib1g-dev  
  
##############  
#SAMTOOLS 1.0#  
##############  
  
RUN mkdir /opt/samtools/ \  
&& cd /opt/samtools/ \  
&& wget -O samtools-bcftools-htslib-1.0_x64-linux.tar.bz2
'https://downloads.sourceforge.net/project/samtools/samtools/1.0/samtools-
bcftools-htslib-1.0_x64-linux.tar.bz2?r=&ts=1506905896&use_mirror=versaweb' \  
&& tar -vxjf samtools-bcftools-htslib-1.0_x64-linux.tar.bz2 \  
&& ln -s /opt/samtools/samtools-bcftools-htslib-1.0_x64-linux/bin/samtools
/usr/bin/samtools \  
&& rm samtools-bcftools-htslib-1.0_x64-linux.tar.bz2  
  
##############  
#BOWTIE 2.3.3#  
##############  
  
RUN mkdir /opt/bowtie2/ \  
&& cd /opt/bowtie2 \  
&& wget -O bowtie2-2.3.3-linux-x86_64.zip
'https://downloads.sourceforge.net/project/bowtie-
bio/bowtie2/2.3.3/bowtie2-2.3.3-linux-x86_64.zip?r=&ts=1506899226&use_mirror=cfhcable'
\  
&& unzip bowtie2-2.3.3-linux-x86_64.zip \  
&& ln -s /opt/bowtie2/bowtie2-2.3.3/bowtie2 /usr/bin/bowtie2 \  
&& ln -s /opt/bowtie2/bowtie2-2.3.3/bowtie2-align /usr/bin/bowtie2-align \  
&& ln -s /opt/bowtie2/bowtie2-2.3.3/bowtie2-inspect /usr/bin/bowtie2-inspect \  
&& ln -s /opt/bowtie2/bowtie2-2.3.3/bowtie2-build /usr/bin/bowtie2-build \  
&& rm bowtie2-2.3.3-linux-x86_64.zip  
  
##############  
#TOPHAT 2.1.1#  
##############  
  
RUN mkdir /opt/tophat2/ \  
&& cd /opt/tophat2 \  
&& wget
http://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz
\  
&& tar -xzvf tophat-2.1.1.Linux_x86_64.tar.gz \  
&& ln -s /opt/tophat2/tophat-2.1.1.Linux_x86_64/tophat /usr/bin/tophat2 \  
&& rm tophat-2.1.1.Linux_x86_64.tar.gz  
  
##############  
#HISAT2 2.0.5#  
##############  
  
RUN mkdir /opt/hisat2/ \  
&& wget
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-Linux_x86_64.zip
\  
&& unzip -d /opt/hisat2/ hisat2-2.0.5-Linux_x86_64.zip \  
&& ln -s /opt/hisat2/hisat2-2.0.5/hisat2 /usr/bin/hisat2 \  
&& rm hisat2-2.0.5-Linux_x86_64.zip  
  
#################  
#Sambamba v0.6.4#  
#################  
  
RUN mkdir /opt/sambamba/ \  
&& wget
https://github.com/lomereiter/sambamba/releases/download/v0.6.4/sambamba_v0.6.4_linux.tar.bz2
\  
&& tar --extract --bzip2 --directory=/opt/sambamba
--file=sambamba_v0.6.4_linux.tar.bz2 \  
&& ln -s /opt/sambamba/sambamba_v0.6.4 /usr/bin/sambamba  
  
##############  
#Picard 2.9.0#  
##############  
  
RUN mkdir /opt/picard/ \  
&& wget
https://github.com/broadinstitute/picard/releases/download/2.9.0/picard.jar \  
&& mv picard.jar /opt/picard/  
  
#################  
#StringTie 1.3.3#  
#################  
  
RUN mkdir /opt/stringtie/ \  
&& wget
http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.3.Linux_x86_64.tar.gz \  
&& cd /opt/stringtie \  
&& tar -xzvf /stringtie-1.3.3.Linux_x86_64.tar.gz \  
&& ln -s /opt/stringtie/stringtie-1.3.3.Linux_x86_64/stringtie
/usr/bin/stringtie \  
&& cd / \  
&& rm stringtie-1.3.3.Linux_x86_64.tar.gz  
  
###############  
#Flexbar 3.0.3#  
###############  
  
RUN mkdir -p /opt/flexbar/tmp \  
&& cd /opt/flexbar/tmp \  
&& wget https://github.com/seqan/flexbar/archive/v3.0.3.tar.gz \  
&& wget https://github.com/seqan/seqan/releases/download/seqan-v2.2.0/seqan-
library-2.2.0.tar.xz \  
&& tar xzf v3.0.3.tar.gz \  
&& tar xJf seqan-library-2.2.0.tar.xz \  
&& mv seqan-library-2.2.0/include flexbar-3.0.3 \  
&& cd flexbar-3.0.3 \  
&& cmake . \  
&& make \  
&& cp flexbar /opt/flexbar/ \  
&& cd / \  
&& rm -rf /opt/flexbar/tmp  
  
######  
#Toil#  
######  
RUN pip install --upgrade pip \  
&& pip install toil[cwl]==3.6.0 \  
&& sed -i 's/select\\[type==X86_64 && mem/select[mem/'
/usr/local/lib/python2.7/dist-packages/toil/batchSystems/lsf.py  
  
# Define a timezone so Java works properly  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime \  
&& echo "America/Chicago" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  

