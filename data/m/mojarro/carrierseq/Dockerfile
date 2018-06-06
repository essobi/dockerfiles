# Docker automated build for Carrier Sequencing Analysis  
# Ubuntu 14.04 Base Image  
FROM ubuntu:14.04  
# Update Base Image  
RUN apt-get update  
  
# Install Dependencies  
RUN apt-get install -y git wget build-essential gcc-multilib apt-utils
zlib1g-dev samtools pkg-config python-setuptools python-dev python-tables
python-pip python-tk python-numpy python-scipy  
  
# Install biopython  
RUN pip install biopython  
  
# Install bwa  
RUN git clone https://github.com/lh3/bwa.git /tmp/bwa  
RUN cd /tmp/bwa \  
git checkout v0.7.15 && \  
make  
WORKDIR /tmp/bwa  
RUN cp -p bwa /usr/local/bin && \  
rm -rf /tmp/bwa  
  
# Install seqtk  
RUN git clone https://github.com/lh3/seqtk.git /tmp/seqtk  
RUN cd /tmp/seqtk \  
git checkout v1.2 && \  
make  
WORKDIR /tmp/seqtk  
RUN cp -p seqtk /usr/local/bin && \  
rm -rf /tmp/seqtk  
  
# Install fqtrim  
RUN mkdir /tmp/fqtrim  
RUN wget http://ccb.jhu.edu/software/fqtrim/dl/fqtrim-0.9.5.tar.gz && \  
tar xvfz fqtrim-0.9.5.tar.gz -C /tmp/fqtrim  
WORKDIR /tmp/fqtrim/fqtrim-0.9.5  
RUN make release && \  
cp -p fqtrim /usr/local/bin  
RUN rm -fr /tmp/fqtrim \  
rm fqtrim-0.9.5.tar.gz  
  
# File author/maintainer info  
MAINTAINER Angel Mojarro <mojarro at mit dot edu>  

