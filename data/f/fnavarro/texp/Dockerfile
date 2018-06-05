FROM debian:stretch  
RUN apt-get update  
  
################  
#Install binaries dependencies  
################  
  
RUN apt-get install -y \  
bedtools=2.26.0+dfsg-3 \  
bowtie2=2.3.0-2 \  
fastx-toolkit=0.0.14-3 \  
gawk=1:4.1.4+dfsg-1 \  
git \  
perl \  
python=2.7.13-2 \  
r-base=3.3.3-1 \  
r-base-dev=3.3.3-1 \  
samtools=1.3.1-3 \  
wget  
  
  
################  
#Install Wgsim  
################  
  
RUN mkdir -p /src; \  
cd /src ; \  
git clone https://github.com/lh3/wgsim.git; \  
cd wgsim; \  
gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm; \  
mv wgsim /usr/bin/; \  
cd /;  
  
  
################  
#Download Libraries  
################  
  
RUN mkdir -p /data/library/rep_annotation; \  
cd /data/library/rep_annotation; \  
wget --quiet -c -t0
"http://homes.gersteinlab.org/people/fn64/TeXP/rep_annotation.hg38.tar.bz2" -O
rep_annotation.hg38.tar.bz2; \  
tar xjvf rep_annotation.hg38.tar.bz2; \  
rm -Rf rep_annotation.hg38.tar.bz2  
  
# DEPRECATED: 2017-02-14 \- Only L1 subfamilies RPKM are estimated in the
latest version  
#RUN mkdir -p /data/library/kallisto; \  
# cd /data/library/; \  
# wget --quiet -c -t0
"https://www.dropbox.com/s/bd0vqqyedx7p0jv/kallisto_gencode23.hg38.tar.bz2?dl=1"
-O kallisto_gencode23.hg38.tar.bz2; \  
# tar xjvf kallisto_gencode23.hg38.tar.bz2; \  
# rm -Rf kallisto_gencode23.hg38.tar.bz2  
  
RUN mkdir -p /data/library/bowtie2; \  
cd /data/library/bowtie2; \  
wget --quiet -c -t0
"http://homes.gersteinlab.org/people/fn64/TeXP/bowtie2.hg38.tar.bz2" -O
bowtie2.hg38.tar.bz2; \  
tar xjvf bowtie2.hg38.tar.bz2; \  
rm -Rf bowtie2.hg38.tar.bz2  
  
  
################  
#Install R packages dependencies  
################  
#RUN cd /data/library/; \  
# wget --quiet -c -t0
"https://cloud.r-project.org/src/contrib/Archive/penalized/penalized_0.9-49.tar.gz"
-O penalized_0.9-49.tar.gz; \  
# R CMD INSTALL penalized_0.9-49.tar.gz  
  
RUN echo 'install.packages(c("penalized"), repos="http://cloud.r-project.org",
dependencies=TRUE)' > /tmp/packages.R \  
&& Rscript /tmp/packages.R  
  
################  
#Install TeXP  
################  
  
ADD https://api.github.com/repos/gersteinlab/texp/git/refs/heads/master
version.json  
RUN mkdir -p /src; \  
cd /src ; \  
git clone https://github.com/gersteinlab/texp.git  
RUN chmod +x /src/texp/TeXP.sh /src/texp/TeXP_batch.sh; \  
ln -s /src/texp/TeXP.sh /usr/bin/TeXP; \  
ln -s /src/texp/TeXP.sh /usr/bin/TeXP.sh; \  
ln -s /src/texp/TeXP_batch.sh /usr/bin/TeXP_batch;  
  
  
WORKDIR /src/texp/  
CMD ["/src/texp/TeXP.sh"]  
  
  

