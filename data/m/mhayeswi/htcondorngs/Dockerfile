FROM debian:stretch  
MAINTAINER Mitch Hayes "mitch@mitchhayes.com"  
# Setup a base system  
RUN apt-get update && \  
apt-get install -y bedtools bowtie2 samtools zlib1g-dev curl g++ make wget git
unzip tar gzip bzip2 xz-utils pigz && \  
  
apt-get install -y --no-install-recommends python2.7-dev python-setuptools  
  
#RUN mkdir /usr/local/genome && cd /usr/local/genome  
RUN easy_install pip && pip install BioPython  
  
RUN wget https://github.com/alexdobin/STAR/archive/2.5.3a.tar.gz && \  
tar -xzf 2.5.3a.tar.gz && cd STAR-2.5.3a/source && make STAR && mv STAR
/usr/local/bin  
  
RUN wget https://github.com/nskvir/RepEnrich2/archive/master.zip && \  
unzip master.zip && chmod ugo+rx RepEnrich2-master/RepEnrich* && \  
mv RepEnrich2-master/RepEnrich* /usr/local/bin && \  
rm -Rf RepEnrich2-master master.zip  
  
RUN chmod ugo+rx /usr/local/bin/RepEnrich*  
WORKDIR /home  
  

