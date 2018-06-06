FROM ubuntu:17.10  
RUN apt-get update && \  
apt-get install -y \  
git cmake zlib1g libhdf5-dev build-essential wget curl unzip jq \  
bc openjdk-8-jre perl unzip r-base libxml2-dev aria2 subread \  
libcurl4-openssl-dev python3-pip python-pip gawk samtools rna-star picard-
tools && \  
apt-get clean  
  
# kallisto 0.44.0  
RUN aria2c
https://github.com/pachterlab/kallisto/releases/download/v0.44.0/kallisto_linux-v0.44.0.tar.gz
&& \  
tar zxf kallisto_linux-v0.44.0.tar.gz && \  
cp kallisto_linux-v0.44.0/kallisto /usr/bin && \  
rm -rf kallisto_linux-v0.44.0/kallisto  
  
# fastqc 0.11.7  
ADD
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip
/tmp/  
RUN cd /usr/local && \  
unzip /tmp/fastqc_*.zip && \  
chmod 755 /usr/local/FastQC/fastqc && \  
ln -s /usr/local/FastQC/fastqc /usr/local/bin/fastqc && \  
rm -rf /tmp/fastqc_*.zip  
  
# gnu parallel  
RUN aria2c http://ftpmirror.gnu.org/parallel/parallel-20170922.tar.bz2 && \  
bzip2 -dc parallel-20170922.tar.bz2 | tar xvf - && \  
cd parallel-20170922 && \  
./configure && make && make install && \  
cd .. && rm -rf parallel-20170922*  
  
# multiqc 1.5  
RUN pip3 install multiqc==v1.5  
  
# drop-seq-tools 1.13-3  
ENV DROPSEQPATH /usr/local/drop-seq-tools  
COPY binaries/Drop-seq_tools-1.13-3.zip .  
RUN unzip Drop-seq_tools-1.13-3.zip -d /tmp && \  
mv /tmp/Drop-seq_tools-1.13 $DROPSEQPATH && \  
rm Drop-seq_tools-1.13-3.zip  
ENV PATH "$PATH:$DROPSEQPATH"  
# for the sanity of python packages  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  

