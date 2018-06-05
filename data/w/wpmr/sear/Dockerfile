# This Dockerfile is used to build the SEAR docker image.  
  
FROM ubuntu:14.04  
MAINTAINER Will Rowe <wpmr2@cam.ac.uk>  
  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
make \  
samtools \  
ncbi-blast\+ \  
bwa \  
tophat \  
seqtk \  
r-base \  
libJSON-perl \  
automake \  
nano  
  
RUN git clone git://github.com/wpmr2/SEAR /tmp/SEAR && mv
/tmp/SEAR/SEAR.docker_version/SEAR / && cp
/tmp/SEAR/SEAR.docker_version/BaseSpace_scripts/perl_parser.pl /usr/bin/ && cp
/tmp/SEAR/SEAR.docker_version/BaseSpace_scripts/vcfutils.pl /usr/bin/ && cp
/SEAR/Sear.pm /usr/lib/perl5/  
RUN git clone git://github.com/torognes/vsearch && cd vsearch && ./configure
&& aclocal && automake && make && make install && cp ./bin/vsearch /usr/bin/
&& cd  
  
ENV PATH /SEAR:$PATH  
  

