FROM viapath/snappy_base:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# fastqc  
RUN wget --no-verbose -O /tmp/fastqc_v0.11.2.zip
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.2.zip &&
\  
unzip /tmp/fastqc_v0.11.2.zip -d /usr/local/pipeline/ && \  
chmod 755 /usr/local/pipeline/FastQC/fastqc && \  
sed -i
'$aCLASSPATH=.:$CLASSPATH:/usr/local/pipeline/FastQC/jbzip2-0.9.jar:/usr/local/pipeline/FastQC/sam-1.103.jar'
/home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/FastQC && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
CMD ["/bin/bash"]  

