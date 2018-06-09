FROM ubuntu:latest  
MAINTAINER brandon850105@gmail.com  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
curl \  
python-minimal \  
wget  
  
  
  
  
# install perl and gcc  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
perl-base vim cpanminus make less gcc \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download & install BLAST  
RUN mkdir /opt/blast \  
&& curl ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz \  
| tar -zxC /opt/blast \--strip-components=1  
  
# install perl module for update_blastdb.pl  
RUN cpan install  
  
RUN mkdir /db /blast  
  
ENV PATH /opt/blast/bin:$PATH  
  
  
  
# set default behaviour  
WORKDIR /blast  
CMD ["bash"]  

