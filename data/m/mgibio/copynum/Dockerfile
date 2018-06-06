FROM ubuntu:xenial  
MAINTAINER Megan Neveau <mnneveau@wustl.edu>  
  
LABEL \  
description="Image for copy number workflow"  
  
RUN apt-get update -y && apt-get install -y \  
wget \  
git \  
unzip \  
bzip2 \  
g++ \  
make \  
zlib1g-dev \  
ncurses-dev \  
python \  
default-jdk \  
default-jre \  
libncurses5-dev  
  
###############  
#Varscan 2.4.2#  
###############  
ENV VARSCAN_INSTALL_DIR=/opt/varscan  
  
WORKDIR $VARSCAN_INSTALL_DIR  
RUN wget
https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar
&& \  
ln -s VarScan.v2.4.2.jar VarScan.jar  
  
#Don't think I need  
#COPY intervals_to_bed.pl /usr/bin/intervals_to_bed.pl  
#COPY varscan_helper.sh /usr/bin/varscan_helper.sh  
################  
#Samtools 1.5#  
################  
RUN apt-get update -y && apt-get install -y libbz2-dev \  
liblzma-dev  
  
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
&& \  
tar --bzip2 -xf samtools-1.5.tar.bz2  
  
WORKDIR /tmp/samtools-1.5  
RUN ./configure --prefix=$SAMTOOLS_INSTALL_DIR && \  
make && \  
make install  
  
WORKDIR /  
RUN rm -rf /tmp/samtools-1.5  
  
##add to top  
RUN apt-get update -y && apt-get install -y python-pip  
RUN pip install --upgrade pip  
  
######  
#Toil#  
######  
RUN pip install toil[cwl]==3.6.0  
RUN sed -i 's/select\\[type==X86_64 && mem/select[mem/'
/usr/local/lib/python2.7/dist-packages/toil/batchSystems/lsf.py  
  
RUN apt-get update -y && apt-get install -y libnss-sss tzdata  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime  
  
#LSF: Java bug that need to change the /etc/timezone.  
# The above /etc/localtime is not enough.  
RUN echo "America/Chicago" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
###  
#R#  
###  
RUN apt-get update -y && apt-get install -y r-base littler  
  
ADD rpackage.R /tmp/  
RUN R -f /tmp/rpackage.R  
  
############  
#scripts#  
############  
COPY /py_scripts/copy_num.py /opt/copy_num/copy_num.py  
COPY /py_scripts/combine.py /opt/copy_num/combine.py  
COPY /py_scripts/get_norm_tum_ratio.py /opt/copy_num/get_norm_tum_ratio.py  
COPY /py_scripts/parse_regions.py /opt/copy_num/parse_regions.py  
COPY /py_scripts/process_results.py /opt/copy_num/process_results.py  
COPY /py_scripts/recenter.py /opt/copy_num/recenter.py  
COPY /py_scripts/seg_combine.py /opt/copy_num/seg_combine.py  
COPY /py_scripts/split.py /opt/copy_num/split.py  
COPY clean_helper.sh /opt/copy_num/clean_helper.sh  
  
###########  
#merge_seg#  
###########  
RUN apt-get update -y && apt-get install -y perl-doc  
COPY mergeCbsSegsFuzzyLog2.pl /usr/bin/mergeCbsSegsFuzzyLog2.pl  
RUN chmod 666 /usr/bin/mergeCbsSegsFuzzyLog2.pl  
  

