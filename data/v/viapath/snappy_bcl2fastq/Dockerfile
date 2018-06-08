FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
## bcl2fastq2 2.17  
ENV TMP /tmp/bcl2fastq  
ENV INSTALL_DIR /usr/local/bin  
  
RUN apt-get update && apt-get install -y alien dpkg-dev debhelper build-
essential  
  
RUN mkdir -p ${TMP} && \  
cd ${TMP} && \  
wget ftp://webdata2:webdata2@ussd-
ftp.illumina.com/downloads/software/bcl2fastq/bcl2fastq2-v2.17.1.14-Linux-x86_64.zip
&& \  
unzip bcl2fastq2-v2.17.1.14-Linux-x86_64.zip && \  
alien bcl2fastq2-v2.17.1.14-Linux-x86_64.rpm && \  
dpkg -i bcl2fastq2_0v2.17.1.14-2_amd64.deb && \  
cd && rm -rf ${TMP}  
  
CMD ["/bin/bash"]  

