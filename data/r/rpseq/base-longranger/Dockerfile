###################################################  
# Dockerfile for Long Ranger  
###################################################  
  
# Based on...  
FROM centos:7  
  
LABEL maintainer "ryan.smith.p@gmail.com"  
  
# Install some utilities  
RUN yum install -y \  
file \  
which \  
sssd-client \  
unzip && \  
yum -y autoremove && \  
yum clean all  
  
# Install bcl2fastq  
RUN cd /tmp/ && \  
curl -o bcl2fastq2-v2.17.1.14-Linux-x86_64.zip ftp://webdata2:webdata2@ussd-
ftp.illumina.com/downloads/software/bcl2fastq/bcl2fastq2-v2.17.1.14-Linux-x86_64.zip
&& \  
unzip bcl2fastq2-v2.17.1.14-Linux-x86_64.zip && \  
yum -y --nogpgcheck localinstall bcl2fastq2-v2.17.1.14-Linux-x86_64.rpm && \  
yum clean all && \  
rm bcl2fastq2-v2.17.1.14-Linux-x86_64.rpm
bcl2fastq2-v2.17.1.14-Linux-x86_64.zip  
  
# Install longranger  
RUN yum install -y git && \  
git clone https://github.com/genome-vendor/10Xgenomics-longranger.git --branch
v2.1.2 --single-branch /opt/longranger-2.1.2/ && \  
rm -rf /opt/longranger-2.1.2/.git && \  
yum -y remove git && \  
yum -y autoremove && \  
yum clean all  

