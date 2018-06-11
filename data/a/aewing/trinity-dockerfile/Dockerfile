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
run apt-get install bowtie -y  
  
## Install Samtools  
run apt-get install samtools -y  
  
RUN echo -n "/trinity" > /etc/container_environment/PATH  
  
ENTRYPOINT ["/sbin/my_init","/bin/bash"]  
  

