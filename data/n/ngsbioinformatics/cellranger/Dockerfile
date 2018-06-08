###############################################  
### Dockerfile for 10X Genomics Cell Ranger ###  
### Derived from https://hub.docker.com/r/litd/docker-cellranger/~/dockerfile/
###  
###############################################  
  
# Based on  
FROM centos:7  
  
# File Author / Maintainer  
MAINTAINER Ryan Golhar <ryan.golhar@bms.com>  
  
# Install some utilities  
RUN yum install -y \  
wget \  
which \  
unzip  
# file \  
# git \  
# sssd-client \  
  
# Install bcl2fastq v2.20  
RUN cd /tmp/ && \  
wget https://support.illumina.com/content/dam/illumina-
support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-linux-x86-64.zip
&& \  
unzip bcl2fastq2-v2-20-0-linux-x86-64.zip && \  
yum install -y --nogpgcheck bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm && \  
rm -f bcl2fastq2-v2-20-0-linux-x86-64.zip
bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm  
  
# Install cellranger v2.02  
RUN cd /opt/ && \  
wget -O cellranger-2.0.2.tar.gz "http://cf.10xgenomics.com/releases/cell-
exp/cellranger-2.0.2.tar.gz?Expires=1507687942&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9jZWxsLWV4cC9jZWxscmFuZ2VyLTIuMC4yLnRhci5neiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTUwNzY4Nzk0Mn19fV19&Signature=EZ3p3o8clI7lmGRVB719N9DFf2jA2qn8BRfbfK7hIzMUtc8v9zUA0NnCKndaDkrBQFyxY18ETdeKnqFTkcBcK44ucIGaVBJG6~IFLoAABMhLBxt6LhTQKzQKlJewJXZx0TuTATGxtlHqGRHO76o1dRl8Ppl0biCWqQ2HqnB47Z1eAvBUfQH-~kmDr8TixjQhSsGQC8WRQWR9VWN1ph4IyiBlHK11AwGCiGSkHgnWUy27-UwdyS1iuct8vvq0Py7tkLNNvx1T89RIGzYF8TTpus9A0K5gQN38rOZx4eUOfERrcm1fq1mjQGAgEg6E38S32utOAvmKoc3bEGZ3EoLCXQ__&Key-
Pair-Id=APKAI7S6A5RYOXBWRPDA" && \  
tar zxvf cellranger-2.0.2.tar.gz && \  
rm -f cellranger-2.0.2.tar.gz  
  
# path  
ENV PATH /opt/cellranger-2.0.2:$PATH  
  

