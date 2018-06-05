FROM phusion/baseimage  
  
MAINTAINER Timothy Laurent timothyjlaurent@gmail.com  
  
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
  
RUN echo -n "/trinity" > /etc/container_environment/PATH  
  
ENTRYPOINT ["/sbin/my_init","--"]  

