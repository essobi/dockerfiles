FROM centos:centos6  
LABEL maintainer "Nathaniel Watson nathankw@stanford.edu"  
  
#Folders /srv/src and /srv/software were created in the base image.  
#ncbi-blast-2.6.0  
#Intall rpm  
RUN curl -O ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-
blast-2.6.0+-1.x86_64.rpm && yum install -y ncbi-blast-2.6.0+-1.x86_64.rpm &&
rm ncbi-blast-2.6.0+-1.x86_64.rpm  
  

