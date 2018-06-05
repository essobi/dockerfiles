## base image  
FROM ubuntu:16.10  
## label  
LABEL version="0.8" \  
maintainer="Johannes Elias" \  
maintainer_email="joheli@gmx.net" \  
description="Image used at DGHM workshop for genome assembly and annotation in
Braunschweig in May 2017" \  
dockerfile_url="https://github.com/dghm-genomics/docker-workshop-
braunschweig/blob/master/Dockerfile" \  
worskhop_url="https://www.dsmz.de/home/news-and-events/events/genomics-
workshop.html"  
  
## packages  
RUN apt-get -y update && apt-get install -y \  
bc \  
bioperl \  
build-essential \  
bwa \  
checkinstall \  
curl \  
default-jre \  
dos2unix \  
gawk \  
git \  
libdatetime-perl \  
libdigest-md5-perl \  
libncurses5-dev \  
libxml-simple-perl \  
lynx \  
man-db \  
mc \  
most \  
nano \  
less \  
pandoc \  
parallel \  
perl \  
python3 \  
python-setuptools \  
sudo \  
varscan \  
vim \  
wget \  
zlib1g-dev  
  
# add user 'workshop-user'  
RUN useradd -ms /bin/bash workshop-user && echo "workshop-
user:BraunschweigDGHM" | chpasswd && adduser workshop-user sudo  
  
## create directories  
WORKDIR /opt  
WORKDIR /home/workshop-user/download  
  
## Help menu  
RUN wget https://github.com/dghm-genomics/docker-workshop-
braunschweig/archive/v0.8.tar.gz; \  
tar -xzf v0.8.tar.gz; \  
mv docker-workshop-braunschweig-0.8 /opt; \  
chmod 755 /opt/docker-workshop-braunschweig-0.8/helpmenu/helpmenu; \  
ln -s /opt/docker-workshop-braunschweig-0.8/helpmenu/helpmenu /usr/bin/  
  
## download and install further software  
# spades  
RUN wget
http://spades.bioinf.spbau.ru/release3.10.1/SPAdes-3.10.1-Linux.tar.gz; \  
tar -xzf SPAdes-3.10.1-Linux.tar.gz; \  
mv SPAdes-3.10.1-Linux /opt; \  
ln -s /opt/SPAdes-3.10.1-Linux/bin/* /usr/bin/  
  
# sratoolkit  
RUN wget https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2/sratoolkit.2.8.2-ubuntu64.tar.gz; \  
tar -xzf sratoolkit.2.8.2-ubuntu64.tar.gz; \  
mv sratoolkit.2.8.2-ubuntu64 /opt; \  
ln -s /opt/sratoolkit.2.8.2-ubuntu64/bin/* /usr/bin/  
  
# Binfo seminar toolbox  
RUN wget https://github.com/dghm-
genomics/Binfo_seminar_toolbox/archive/1.4.tar.gz; \  
tar -xzf 1.4.tar.gz; \  
mv Binfo_seminar_toolbox-1.4 /opt; \  
chmod 755 /opt/Binfo_seminar_toolbox-1.4/*.sh; \  
ln -s /opt/Binfo_seminar_toolbox-1.4/* /usr/bin/  
  
# bbtools  
RUN wget https://sourceforge.net/projects/bbmap/files/latest/download; \  
mv download bbmap.tar.gz; \  
tar -xzf bbmap.tar.gz; \  
mv bbmap /opt; \  
ln -s /opt/bbmap/*.sh /usr/bin/  
  
# barrnap  
RUN wget http://www.vicbioinformatics.com/barrnap-0.6.tar.gz; \  
tar -xzf barrnap-0.6.tar.gz; \  
mv barrnap-0.6 /opt; \  
ln -s /opt/barrnap-0.6/bin/* /usr/bin/  
  
# infernal  
RUN wget http://eddylab.org/infernal/infernal-1.1.2-linux-intel-gcc.tar.gz; \  
tar -xzf infernal-1.1.2-linux-intel-gcc.tar.gz; \  
mv infernal-1.1.2-linux-intel-gcc /opt  
WORKDIR /opt/infernal-1.1.2-linux-intel-gcc  
RUN ./configure; \  
make; \  
make install  
WORKDIR /home/workshop-user/download  
  
# tbl2asn  
RUN wget
ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux.tbl2asn.gz;
\  
gzip -d linux.tbl2asn.gz; \  
mkdir -p /opt/tbl2asn; \  
mv linux.tbl2asn /opt/tbl2asn/tbl2asn; \  
chmod 755 /opt/tbl2asn/tbl2asn; \  
ln -s /opt/tbl2asn/* /usr/bin/  
  
# prodigal  
RUN wget https://github.com/hyattpd/Prodigal/archive/v2.6.3.tar.gz; \  
tar -xzf v2.6.3.tar.gz; \  
mv Prodigal-2.6.3 /opt  
WORKDIR /opt/Prodigal-2.6.3  
RUN make install  
WORKDIR /home/workshop-user/download  
  
# aragorn  
RUN wget http://mbio-serv2.mbioekol.lu.se/ARAGORN/Downloads/aragorn1.2.38.tgz;
\  
tar -xzf aragorn1.2.38.tgz; \  
mv aragorn1.2.38 /opt;  
WORKDIR /opt/aragorn1.2.38  
RUN gcc -O3 -ffast-math -finline-functions -o aragorn aragorn1.2.38.c  
RUN ln -s /opt/aragorn1.2.38/aragorn /usr/bin/  
WORKDIR /home/workshop-user/download  
  
# hmmer & easel  
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-
intel-x86_64.tar.gz; \  
tar -xzf hmmer-3.1b2-linux-intel-x86_64.tar.gz; \  
mv hmmer-3.1b2-linux-intel-x86_64 /opt  
WORKDIR /opt/hmmer-3.1b2-linux-intel-x86_64  
RUN ./configure  
RUN make  
RUN make install  
WORKDIR /opt/hmmer-3.1b2-linux-intel-x86_64/easel  
RUN make install  
WORKDIR /home/workshop-user/download  
  
# prokka  
RUN git clone https://github.com/tseemann/prokka.git; \  
mv prokka /opt; \  
ln -s /opt/prokka/bin/* /usr/bin;\  
prokka --setupdb  
  
# parsnp  
RUN wget https://github.com/marbl/parsnp/releases/download/v1.2/parsnp-
Linux64-v1.2.tar.gz; \  
tar -xvf parsnp-Linux64-v1.2.tar.gz; \  
mv Parsnp-Linux64-v1.2 /opt; \  
ln -s /opt/Parsnp-Linux64-v1.2/parsnp /usr/bin/  
  
# kaiju  
RUN git clone https://github.com/bioinformatics-centre/kaiju.git; \  
mv kaiju /opt  
WORKDIR /opt/kaiju/src  
RUN make; \  
ln -s $(find /opt/kaiju/bin/ -type f -perm /111) /usr/bin  
WORKDIR /home/workshop-user/download  
  
# quast  
RUN wget
https://sourceforge.net/projects/quast/files/quast-4.5.tar.gz/download; \  
mv download quast-4.5.tar.gz; \  
tar -xvf quast-4.5.tar.gz; \  
mv quast-4.5 /opt  
WORKDIR /opt/quast-4.5  
RUN ./setup.py install  
WORKDIR /home/workshop-user/download  
  
# samtools 0.1.19  
RUN wget
https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download;
\  
mv download samtools.tar.bz2; \  
tar xfj samtools.tar.bz2; \  
chmod 755 samtools-0.1.19; \  
mv samtools-0.1.19 /opt  
WORKDIR /opt/samtools-0.1.19  
RUN make; \  
mv /usr/bin/samtools /usr/bin/samtools-1.3.1; \  
chmod 777 samtools; \  
ln -s /opt/samtools-0.1.19/samtools /usr/bin/  
  
## set rights & change user  
RUN chown -R workshop-user:workshop-user /home/workshop-user/*  
USER workshop-user  
WORKDIR /home/workshop-user  
  
## Download raw data  
# Mycoplasma genitalium genomes (from SRA)  
RUN prefetch ERR486835; \  
prefetch ERR486836  

