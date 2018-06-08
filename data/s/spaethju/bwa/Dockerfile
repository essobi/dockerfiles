# Set the base image to centos  
FROM centos:7  
# Set working directory (is synchronized with host data folder)  
WORKDIR /data  
  
# Update OS and install wget  
RUN yum -y update  
RUN yum -y upgrade  
RUN yum -y install wget  
  
# Install bwa and samtools  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install epel-release-latest-7.noarch.rpm  
RUN yum -y install bwa  
  
#Run bwa and samtools  
ENTRYPOINT bwa index ${FASTA} && \  
bwa mem -t ${THREADS} -k ${SEED_LEN} -A ${MATCH} -B ${MISMATCH} -O ${GAP_OPEN}
-E ${GAP_EXT} ${FASTA} ${FASTQ} > ${SAM}  

