# Set the base image to centos  
FROM centos:7  
# Set working directory (is synchronized with host data folder)  
WORKDIR /data  
  
# Update OS and install wget  
RUN yum -y update  
RUN yum -y upgrade  
RUN yum -y install wget  
  
# Install samtools  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install epel-release-latest-7.noarch.rpm  
RUN yum -y install samtools  
  
#Run samtools  
ENTRYPOINT samtools view -bS ${SAM} | samtools sort - ${BAM::-4} && \  
samtools view -F 0x10 -b ${BAM} > ${POSITIVE} && \  
samtools view -f 0x10 -b ${BAM} > ${NEGATIVE}  

