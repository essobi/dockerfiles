FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
## bowtie  
RUN wget -O /tmp/bowtie2-2.2.3-linux-x86_64.zip
http://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip && \  
unzip /tmp/bowtie2-2.2.3-linux-x86_64.zip -d /usr/local/pipeline/ && \  
sed -i
'$aPATH=$PATH:/usr/local/pipeline/bowtie2-2.2.3:/usr/local/pipeline/bowtie2-2.2.3/scripts'
/home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/bowtie2-2.2.3 && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
# BWA  
RUN cd /tmp && wget \--no-verbose http://sourceforge.net/projects/bio-
bwa/files/bwa-0.7.12.tar.bz2 && \  
tar xjvf /tmp/bwa-0.7.12.tar.bz2 && \  
cd bwa-0.7.12 && make && \  
mkdir -p /usr/local/pipeline/bwa-0.7.12/ && cp bwa
/usr/local/pipeline/bwa-0.7.12/ && \  
ln -s /usr/local/pipeline/bwa-0.7.12/bwa /usr/local/bin/ && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/bwa-0.7.12' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/bwa-0.7.12 && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
# Stampy  
RUN wget -O /tmp/stampy-latest.tgz
http://www.well.ox.ac.uk/bioinformatics/Software/Stampy-latest.tgz && \  
tar xvfz /tmp/stampy-latest.tgz -C /usr/local/pipeline/ && \  
chmod -R 755 /usr/local/pipeline/stampy-1.0.28 && \  
cd /usr/local/pipeline/stampy-1.0.28 && \  
make && \  
sed -i '$aPATH=${PATH}:/usr/local/pipeline/stampy-1.0.28' /home/snappy/.bashrc
&& \  
chmod -R 755 /usr/local/pipeline/stampy-1.0.28 && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rf /tmp/*  
  
# ABRA realignment  
RUN mkdir /usr/local/pipeline/abra && \  
wget \--no-verbose -O /usr/local/pipeline/abra/abra-0.94-SNAPSHOT-jar-with-
dependencies.jar \  
https://github.com/mozack/abra/releases/download/v0.94/abra-0.94-SNAPSHOT-jar-
with-dependencies.jar && \  
sed -i '$aCLASSPATH=.:$CLASSPATH:/usr/local/pipeline/abra/abra-0.94-SNAPSHOT-
jar-with-dependencies.jar' /home/snappy/.bashrc && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/abra' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/abra && \  
chown -R snappy:snappy /usr/local/pipeline  
  
  
CMD ["/bin/bash"]  

