#USE BLAST BINARIES FROM UMMIDOCK REPO  
FROM ummidock/blast_binaries:2.6.0-binaries  
MAINTAINER Diogo N Silva, diogosilva@medicina.ulisboa.pt  
  
WORKDIR /NGStools/  
  
RUN apt-get update && apt-get install -y \  
libmoo-perl \  
liblist-moreutils-perl \  
libjson-perl \  
libfile-slurp-perl \  
file \  
git \  
gzip \  
wget  
  
RUN git clone https://github.com/tseemann/mlst.git  
ENV PATH="/NGStools/mlst/bin:${PATH}"  
# Replace default db with one without yersinia pseudotuberculosis  
RUN wget
https://github.com/tseemann/mlst/files/1856005/db_without_ypseudotuberculosis.tar.gz
&& tar xf db_without_ypseudotuberculosis.tar.gz  
RUN rm -r mlst/db && mv db mlst/db  

