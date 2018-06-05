#################################################################  
# Dockerfile  
#  
# Version: 0.0.1  
# Software: blast2lca  
# Software Version: 0.0.1  
# Description: converts diamond output into ko and taxid tables  
# Website: https://github.com/etheleon/blast2lcaplus  
# Tags: Genomics Metagenomics  
# Provides: Megan CE  
# Base Image: ubuntu:16.04  
# Run CMD:  
#  
# docker run --rm \  
# -v $PWD:/data \  
# -v
/export2/home/uesu/simulation_fr_the_beginning/reAssemble/everybodyelse/out/diamond/nr_trimmed/trimmed_contig.m8:/data/diamond.m8
\  
# -v
/export2/home/uesu/simulation_fr_the_beginning/data/classifier/gi2taxid.refseq.map:/data/gi2kegg
\  
# -v /export2/home/uesu/github/MEGAN/tools/gi2kegg.map:/data/gi2taxid \  
# etheleon/blast2lca:latest  
# interactive  
# docker run --rm -it \  
# -v $PWD:/data \  
# -v
/export2/home/uesu/simulation_fr_the_beginning/reAssemble/everybodyelse/out/diamond/nr_trimmed/trimmed_contig.m8:/data/diamond.m8
\  
# -v
/export2/home/uesu/simulation_fr_the_beginning/data/classifier/gi2taxid.refseq.map:/data/gi2kegg
\  
# -v /export2/home/uesu/github/MEGAN/tools/gi2kegg.map:/data/gi2taxid \  
# --entrypoint /bin/bash \  
# etheleon/blast2lca:latest  
################################################################  
  
FROM ubuntu:16.04  
MAINTAINER wesley goi <picy2k@gmail.com>  
  
#Java###############################  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer git bzip2 && \  
apt-get clean  
  
#python##############################  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > $HOME/.bashrc && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
#MEGAN6-CE#############################  
WORKDIR /tmp  
RUN wget http://ab.inf.uni-
tuebingen.de/data/software/megan6/download/MEGAN_Community_unix_6_8_12.sh  
RUN perl -E 'say join "\n", "", 1, "", "1,2,3", "", "", "", 38000, n, ""' >
/tmp/megan_install_v6  
RUN bash MEGAN_Community_unix_6_8_12.sh < /tmp/megan_install_v6  
  
#Blast2lcaplus########################  
RUN git clone https://github.com/etheleon/blast2lcaPlus /tmp/blast2lcaPlus  
ENV PATH="/opt/conda/bin:${PATH}"  
  
VOLUME ["/data"]  
ENTRYPOINT ["/tmp/blast2lcaPlus/fullPipeline"]  
CMD ["/data", ".", "query", "diamond.m8", "taxOutput", "koOutput", "--
blast2lca", "/opt/megan/tools/blast2lca", "--gi2kegg", "/data/gi2kegg", "--
gi2taxid", "/data/gi2taxid"]  

