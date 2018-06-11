FROM phusion/baseimage  
  
MAINTAINER Aren Ewing aren.ewing@gmail.com  
  
RUN apt-get update;\  
apt-get install -y -q wget;\  
apt-get install -y -q openjdk-7-jre;\  
apt-get clean  
  
## Install Trinity  
RUN mkdir /trinity && cd /trinity;\  
wget
http://sourceforge.net/projects/trinityrnaseq/files/trinityrnaseq_r20140413p1.tar.gz;\  
apt-get update; apt-get install -y -q build-essential;\  
apt-get install -y -q zlib1g-dev && apt-get clean;\  
tar -xaf trinity*; rm -rf *.gz;\  
cp -r trinityrnaseq_r20140413p1/* ./;\  
rm -rf trinityrnaseq_r20140413p1;\  
make  
  
## Install FastqMCF  
RUN apt-get update ; apt-get install -y subversion libgsl0-dev; apt-get
clean;\  
svn checkout http://ea-utils.googlecode.com/svn/trunk/ ea-utils-read-only ;\  
cd ea-utils-read-only/clipper ;\  
make install;\  
cd ../..; rm -rf ea-utils-read-only  
  
## Install Bowtie2  
RUN apt-get update;\  
apt-get install bowtie -y ;\  
apt-get clean  
  
## Install Samtools  
RUN apt-get update;\  
apt-get install samtools -y ;\  
apt-get clean  
  
## Install Hmmer/Pfam  
RUN apt-get update;\  
apt-get install hmmer ;\  
apt-get clean  
  
## Install Blast+  
RUN mkdir /blast && cd /blast;\  
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.29/ncbi-
blast-2.2.29+-x64-linux.tar.gz ;\  
tar zxvpf ncbi-blast-2.2.29+-x64-linux.tar.gz ;\  
rm ncbi-blast-2.2.29+-x64-linux.tar.gz ;\  
cd ..  
  
## Install sqlite  
RUN apt-get update;\  
apt-get install sqlite -y ;\  
apt-get clean  
  
## Install Trinotate  
RUN mkdir /trinotate && cd /trinotate;\  
wget
http://downloads.sourceforge.net/project/trinotate/Trinotate_r20140708.tar.gz
;\  
tar xzvf Trinotate_r20140708.tar.gz ;\  
rm Trinotate_r20140708.tar.gz ;\  
cd ..  
  
## Install perl URI:Escape module  
RUN apt-get install -y cpanminus ;\  
cpanm -v URI::Escape ;\  
cpanm -v DBI ;\  
cpanm -v DBD::SQLite ;\  
cpanm -v PerlIO::gzip  
  
env PATH /trinity:/blast/ncbi-
blast-2.2.29+/bin:/trinotate/Trinotate_r20140708:$PATH  
  
ENTRYPOINT ["/sbin/my_init","/bin/bash"]  
  

