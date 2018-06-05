#  
# Installing UCSC-BLAT with the hg19 2bit-file  
# http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/  
# Please note that the Blat source and executables are freely available for  
# academic, nonprofit and personal use. Commercial licensing information is  
# available on the Kent Informatics website (http://www.kentinformatics.com/).  
#  
# version 0.1  
FROM ubuntu:14.04  
MAINTAINER MISHIMA, Hiroyuki <missy@be.to>  
  
RUN apt-get update  
RUN apt-get -y install wget  
RUN mkdir -p /opt/BLAT  
RUN wget --timestamping
'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit' -P /opt/BLAT  
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat -P
/opt/BLAT  
RUN chmod a+x /opt/BLAT/blat  
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/gfClient
-P /opt/BLAT  
RUN chmod a+x /opt/BLAT/gfClient  
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/gfServer
-P /opt/BLAT  
RUN chmod a+x /opt/BLAT/gfServer  
RUN apt-get -y install libkrb5-3  
  
CMD /opt/BLAT/gfServer start localhost 55519 /opt/BLAT/hg19.2bit -canStop  
  

