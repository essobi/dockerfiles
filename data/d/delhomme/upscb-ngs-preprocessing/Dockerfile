FROM delhomme/upscb-jbrowse  
MAINTAINER Nicolas Delhomme (nicolas.delhomme@umu.se)  
  
#########  
### Aptitude packages  
#########  
RUN apt-get update && apt-get install -y default-jre wget git ftp nano
python2.7-dev python-pip openssl openssh-server \  
libcairo2-dev libpango1.0-dev liblzma-dev libbz2-dev  
  
#########  
### Working dir  
#########  
RUN mkdir build  
WORKDIR /build  
  
#########  
### Java tools: Trimmomatic, FastQC  
#########  
RUN wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip &&
\  
unzip fastqc_v0.11.7.zip && \  
chmod +x FastQC/fastqc && \  
cp -r FastQC /usr/share/ && \  
ln -s /usr/share/FastQC/fastqc /usr/bin/ && \  
wget
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
&& \  
unzip Trimmomatic-0.36.zip && \  
cp -r Trimmomatic-0.36 /usr/share/ && \  
echo '#!/bin/bash\njava -jar /usr/share/Trimmomatic-0.36/trimmomatic-0.36.jar
$@' > /usr/bin/trimmomatic && \  
chmod +x /usr/bin/trimmomatic  
  
#########  
### SortmeRNA  
#########  
RUN wget https://github.com/biocore/sortmerna/archive/2.1b.tar.gz && \  
tar -xf 2.1b.tar.gz  
WORKDIR sortmerna-2.1b  
RUN ./configure && make && make install || true  
RUN cp indexdb_rna /usr/local/bin && \  
cp scripts/merge-paired-reads.sh /usr/local/bin && cp scripts/unmerge-paired-
reads.sh /usr/local/bin && \  
cp -r rRNA_databases/ /usr/share/  
WORKDIR /usr/share/rRNA_databases  
ADD scripts/phiX.fasta /usr/share/rRNA_databases/phiX.fasta  
COPY scripts/indexdb.sh /usr/share/rRNA_databases/  
COPY scripts/makeDbList.sh /usr/share/rRNA_databases/  
RUN ./indexdb.sh  
ENV SORTMERNA_DB="/usr/share/rRNA_databases/rfam-5s-database-
id98.fasta,/usr/share/rRNA_databases/index/rfam-5s-database-
id98:/usr/share/rRNA_databases/silva-
euk-28s-id98.fasta,/usr/share/rRNA_databases/index/silva-
euk-28s-id98:/usr/share/rRNA_databases/silva-
euk-18s-id95.fasta,/usr/share/rRNA_databases/index/silva-
euk-18s-id95:/usr/share/rRNA_databases/silva-
arc-16s-id95.fasta,/usr/share/rRNA_databases/index/silva-
arc-16s-id95:/usr/share/rRNA_databases/silva-
bac-16s-id90.fasta,/usr/share/rRNA_databases/index/silva-
bac-16s-id90:/usr/share/rRNA_databases/silva-
arc-23s-id98.fasta,/usr/share/rRNA_databases/index/silva-
arc-23s-id98:/usr/share/rRNA_databases/silva-
bac-23s-id98.fasta,/usr/share/rRNA_databases/index/silva-
bac-23s-id98:/usr/share/rRNA_databases/rfam-5.8s-database-
id98.fasta,/usr/share/rRNA_databases/index/rfam-5.8s-database-
id98:/usr/share/rRNA_databases/phiX.fasta,/usr/share/rRNA_databases/index/phiX"  
RUN echo "export SORTMERNA_DB=$SORTMERNA_DB" >> /home/training/.profile  
WORKDIR /build  
  
#########  
### Pip installs: multiQC  
#########  
RUN git clone https://github.com/ewels/MultiQC && cd MultiQC && \  
pip install numpy matplotlib && \  
python setup.py install  
  
RUN wget http://genometools.org/pub/genometools-1.5.10.tar.gz && \  
tar -xf genometools-1.5.10.tar.gz && cd genometools-1.5.10 && \  
make && make install  
  
#########  
### HTSlib tools: Samtools, Bcftools  
#########  
WORKDIR /build  
RUN wget
https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2
\  
https://github.com/samtools/bcftools/releases/download/1.7/bcftools-1.7.tar.bz2
\  
https://github.com/samtools/htslib/releases/download/1.7/htslib-1.7.tar.bz2 &&
\  
tar -xf htslib-1.7.tar.bz2  
WORKDIR htslib-1.7  
RUN ./configure && make && make install  
WORKDIR /build  
RUN tar -xf bcftools-1.7.tar.bz2  
WORKDIR bcftools-1.7  
RUN make && make install  
WORKDIR /build  
RUN tar -xf samtools-1.7.tar.bz2  
WORKDIR samtools-1.7  
RUN make && make install  
WORKDIR /build  
  
#########  
### bedtools  
#########  
WORKDIR /build  
RUN wget
https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz
&& \  
tar -xf bedtools-2.27.1.tar.gz && cd bedtools2 && \  
make -j 4 && make install  
  
#########  
### GateOne SSH interface  
#########  
RUN pip install tornado==4.4.3  
RUN git clone https://github.com/liftoff/GateOne/ && \  
cd GateOne && python setup.py install && \  
python run_gateone.py --configure && cd ..  
  
#########  
### Clean up  
#########  
WORKDIR /  
RUN rm -rf /build  
  
#########  
# Apache access to the home dir  
#########  
RUN ln -sf /home/training /var/www/html/home  
  
#########  
### Supervisor  
#########  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#########  
### Volumes  
#########  
RUN mkdir /home/training/share  
VOLUME /home/training/share  
  
#########  
### Ports and CMD  
#########  
EXPOSE 22 443  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

