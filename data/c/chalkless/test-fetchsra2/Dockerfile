# Docker container for fetching FASTQ files  
FROM ubuntu  
  
MAINTAINER Takeru Nakazato, chalkless@gmail.com  
  
# Copy fetch script  
ADD fetchsra.pl fetchsra.pl  
  
# Install Packages  
RUN apt-get update && \  
apt-get install -y wget  
  
# Download SRA ID table  
RUN wget ftp://ftp-
trace.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab  
  
ENTRYPOINT ["./fetchsra.pl"]  
  

