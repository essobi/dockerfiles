FROM ubuntu:xenial  
MAINTAINER Megan Neveau <mnn6412@truman.edu>  
  
LABEL \  
description="Image for Concordance tool"  
  
RUN apt-get update -y && apt-get install -y \  
wget \  
git \  
unzip \  
python \  
python-dev \  
python-pip \  
emacs  
  
#############  
#Concordance#  
#############  
COPY newConcordance.py /opt/concordance/newConcordance.py  
  
###############  
#bam-readcount#  
###############  
RUN apt-get update && \  
apt-get install -y \  
cmake \  
patch  
  
ENV SAMTOOLS_ROOT=/opt/samtools  
RUN mkdir /opt/bam-readcount  
  
WORKDIR /opt/bam-readcount  
RUN git clone https://github.com/genome/bam-readcount.git /tmp/bam-
readcount-0.7.4 && \  
git -C /tmp/bam-readcount-0.7.4 checkout v0.7.4 && \  
cmake /tmp/bam-readcount-0.7.4 && \  
make && \  
rm -rf /tmp/bam-readcount-0.7.4 && \  
ln -s /opt/bam-readcount/bin/bam-readcount /usr/bin/bam-readcount  
  
RUN pip install --upgrade pip  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
gfortran  
  
#COPY bam_readcount_helper.py /usr/bin/bam_readcount_helper.py  
RUN pip install cyvcf2  
  
####################  
#Fisher Python Test#  
####################  
RUN pip install FisherExact  
  
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

