FROM ubuntu  
  
LABEL maintainer "swamidass@gmail.com"  
LABEL version "1.0"  
LABEL website "https://bitbucket.org/swamidass/human-blast"  
LABEL human_genome_version "GRCh38.p10"  
LABEL description "Setup a BLAST database with the full human genome."  
ARG
HUMAN_GENOME=ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.25_GRCh38.p10/GCA_000001405.25_GRCh38.p10_genomic.fna.gz  
  
RUN apt-get -qq update && \  
apt-get -qq install -y curl python ssh ncbi-blast+ && \  
apt-get -qq clean  
  
RUN mkdir /blast  
WORKDIR /blast  
  
RUN curl -s $HUMAN_GENOME > human.fna.gz > human.fna.gz && \  
gunzip human.fna.gz && \  
makeblastdb -in human.fna -dbtype nucl -out human && \  
rm human.fna && \  
apt-get -qq clean  

