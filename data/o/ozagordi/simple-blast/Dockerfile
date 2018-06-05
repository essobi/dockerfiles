FROM ubuntu:14.04  
MAINTAINER osvaldo.zagordi@gmail.com  
  
RUN apt-get update -y && apt-get install -y \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN wget -q -O -
ftp://ftp.ncbi.nlm.nih.gov/blast//executables/blast+/2.3.0/ncbi-
blast-2.3.0+-x64-linux.tar.gz | \  
tar -xvz  
  
WORKDIR /tmp/ncbi-blast-2.3.0+/bin  
  
RUN install makeblastdb blastn blastp blastx tblastn tblastx /usr/local/bin/  
WORKDIR /home  
RUN rm -rf /tmp/ncbi-blast-2.3.0+  
# set default behaviour  
#CMD ["bash"]  

