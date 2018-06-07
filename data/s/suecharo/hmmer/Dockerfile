# Docker image for HMMER  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update && apt-get install -y \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install HMMER  
WORKDIR /src  
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-
intel-x86_64.tar.gz \  
&& tar zxvf hmmer-3.1b2-linux-intel-x86_64.tar.gz \  
&& rm -rf hmmer-3.1b2-linux-intel-x86_64.tar.gz \  
&& ln -s /src/hmmer-3.1b2-linux-intel-x86_64/binaries/* /usr/local/bin/  
  
# Setup Pfam  
WORKDIR /src  
RUN wget
ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam31.0/Pfam-A.hmm.gz \  
&& gzip -d Pfam-A.hmm.gz \  
&& hmmpress Pfam-A.hmm  
  
WORKDIR /mount  
CMD ["bash"]  

