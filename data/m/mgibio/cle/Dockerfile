FROM ubuntu:xenial  
MAINTAINER Susanna Kiwala <ssiebert@wustl.edu>  
  
LABEL \  
description="Image for tools used in the CLE"  
  
RUN apt-get update -y && apt-get install -y \  
ant \  
apt-utils \  
bioperl \  
build-essential \  
bzip2 \  
curl \  
default-jdk \  
default-jre \  
gcc-multilib \  
git \  
g++ \  
libfile-copy-recursive-perl \  
libarchive-extract-perl \  
libarchive-zip-perl \  
libapache-dbi-perl \  
libmodule-build-perl \  
libncurses5-dev \  
make \  
ncurses-dev \  
nodejs \  
perl-doc \  
python \  
python-dev \  
python3 \  
python3-pip \  
rsync \  
unzip \  
wget \  
zlib1g-dev  
  
RUN apt-get update -y && apt-get install -y python-pip python-dev build-
essential nodejs  
RUN pip install --upgrade pip  
  
RUN ln -s /usr/bin/unzip /bin/unzip  
  
##########  
#GATK 3.5#  
##########  
RUN cd /tmp/ \  
&& wget -O /tmp/gatk3.5.tar.bz2
'https://software.broadinstitute.org/gatk/download/auth?package=GATK-
archive&version=3.5-0-g36282e4' \  
&& tar xf gatk3.5.tar.bz2 \  
&& cp GenomeAnalysisTK.jar /opt/GenomeAnalysisTK-3.5.jar \  
&& rm -rf /tmp/*  
  
##########  
#GATK 3.6#  
##########  
ENV maven_package_name apache-maven-3.3.9  
ENV gatk_dir_name gatk-protected  
ENV gatk_version 3.6  
RUN cd /tmp/ && wget -q
http://mirror.nohup.it/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.zip  
  
# LSF: Comment out the oracle.jrockit.jfr.StringConstantPool.  
RUN cd /tmp/ \  
&& git clone \--recursive https://github.com/broadgsa/gatk-protected.git \  
&& cd /tmp/gatk-protected && git checkout tags/${gatk_version} \  
&& sed -i 's/^import oracle.jrockit.jfr.StringConstantPool;/\/\/import
oracle.jrockit.jfr.StringConstantPool;/' ./public/gatk-tools-
public/src/main/java/org/broadinstitute/gatk/tools/walkers/varianteval/VariantEval.java
\  
&& mv /tmp/gatk-protected /opt/${gatk_dir_name}-${gatk_version}  
RUN cd /opt/ && unzip /tmp/${maven_package_name}-bin.zip \  
&& rm -rf /tmp/${maven_package_name}-bin.zip LICENSE NOTICE README.txt \  
&& cd /opt/ \  
&& cd /opt/${gatk_dir_name}-${gatk_version} &&
/opt/${maven_package_name}/bin/mvn verify -P\\!queue \  
&& mv /opt/${gatk_dir_name}-${gatk_version}/protected/gatk-package-
distribution/target/gatk-package-distribution-${gatk_version}.jar
/opt/GenomeAnalysisTK.jar \  
&& rm -rf /opt/${gatk_dir_name}-${gatk_version} /opt/${maven_package_name}  
  
###############  
#Strelka 2.7.1#  
###############  
ENV STRELKA_INSTALL_DIR /opt/strelka/  
  
RUN wget
https://github.com/Illumina/strelka/releases/download/v2.7.1/strelka-2.7.1.centos5_x86_64.tar.bz2
\  
&& tar xf strelka-2.7.1.centos5_x86_64.tar.bz2 \  
&& rm -f strelka-2.7.1.centos5_x86_64.tar.bz2 \  
&& mv strelka-2.7.1.centos5_x86_64 $STRELKA_INSTALL_DIR  
  
#strelka requires a couple steps to run, so add a helper script to sequence
those  
COPY strelka_helper.pl /usr/bin/strelka_helper.pl  
COPY add_strelka_gt.pl /usr/bin/add_strelka_gt.pl  
  
###############  
#Varscan 2.4.2#  
###############  
ENV VARSCAN_INSTALL_DIR=/opt/varscan  
  
WORKDIR $VARSCAN_INSTALL_DIR  
RUN wget
https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar
&& \  
ln -s VarScan.v2.4.2.jar VarScan.jar  
  
COPY intervals_to_bed.pl /usr/bin/intervals_to_bed.pl  
COPY varscan_helper.sh /usr/bin/varscan_helper.sh  
COPY varscan_germline_helper.sh /usr/bin/varscan_germline_helper.sh  
  
##############  
#HTSlib 1.3.2#  
##############  
ENV HTSLIB_INSTALL_DIR=/opt/htslib  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2
&& \  
tar --bzip2 -xvf htslib-1.3.2.tar.bz2  
  
WORKDIR /tmp/htslib-1.3.2  
RUN ./configure --enable-plugins --prefix=$HTSLIB_INSTALL_DIR && \  
make && \  
make install && \  
cp $HTSLIB_INSTALL_DIR/lib/libhts.so* /usr/lib/  
  
################  
#Samtools 1.3.1#  
################  
ENV SAMTOOLS_INSTALL_DIR=/opt/samtools  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar --bzip2 -xf samtools-1.3.1.tar.bz2  
  
WORKDIR /tmp/samtools-1.3.1  
RUN ./configure --with-htslib=$HTSLIB_INSTALL_DIR
\--prefix=$SAMTOOLS_INSTALL_DIR && \  
make && \  
make install  
  
WORKDIR /  
RUN rm -rf /tmp/samtools-1.3.1  
  
#################  
#Sambamba v0.6.4#  
#################  
RUN mkdir /opt/sambamba/ \  
&& wget
https://github.com/lomereiter/sambamba/releases/download/v0.6.4/sambamba_v0.6.4_linux.tar.bz2
\  
&& tar --extract --bzip2 --directory=/opt/sambamba
--file=sambamba_v0.6.4_linux.tar.bz2 \  
&& ln -s /opt/sambamba/sambamba_v0.6.4 /usr/bin/sambamba  
  
############  
#BWA 0.7.15#  
############  
ENV BWA_VERSION 0.7.15  
RUN cd /tmp/ \  
&& wget -q http://downloads.sourceforge.net/project/bio-
bwa/bwa-${BWA_VERSION}.tar.bz2 && tar xvf bwa-${BWA_VERSION}.tar.bz2 \  
&& cd /tmp/bwa-${BWA_VERSION} \  
&& sed -i 's/CFLAGS=\\\t\\\t-g -Wall -Wno-unused-function -O2/CFLAGS=-g -Wall
-Wno-unused-function -O2 -static/' Makefile \  
&& make \  
&& cp /tmp/bwa-${BWA_VERSION}/bwa /usr/local/bin \  
&& rm -rf /tmp/bwa-${BWA_VERSION}  
  
###################  
#Samblaster 0.1.24#  
###################  
RUN cd /tmp/ \  
&& git clone https://github.com/GregoryFaust/samblaster.git \  
&& cd /tmp/samblaster \  
&& git checkout tags/v.0.1.24 \  
&& make \  
&& cp /tmp/samblaster/samblaster /usr/local/bin \  
&& rm -rf /tmp/samblaster  
  
# alignment helper scripts  
COPY alignment_helper.sh /usr/bin/alignment_helper.sh  
COPY markduplicates_helper.sh /usr/bin/markduplicates_helper.sh  
  
################  
#Pindel 0.2.5b8#  
################  
WORKDIR /opt  
RUN wget https://github.com/genome/pindel/archive/v0.2.5b8.tar.gz && \  
tar -xzf v0.2.5b8.tar.gz  
  
WORKDIR /opt/pindel-0.2.5b8  
RUN ./INSTALL /tmp/htslib-1.3.2  
  
WORKDIR /  
RUN rm -rf /tmp/htslib-1.3.2  
RUN ln -s /opt/pindel-0.2.5b8/pindel /usr/bin/pindel  
RUN ln -s /opt/pindel-0.2.5b8/pindel2vcf /usr/bin/pindel2vcf  
  
COPY pindel_helper.pl /usr/bin/pindel_helper.pl  
COPY write_pindel_filter_config.pl /usr/bin/write_pindel_filter_config.pl  
COPY somatic_indelfilter.pl /usr/bin/somatic_indelfilter.pl  
  
###############  
#bam-readcount#  
###############  
RUN apt-get update && \  
apt-get install -y \  
cmake \  
patch \  
git  
  
ENV SAMTOOLS_ROOT=/opt/samtools  
RUN mkdir /opt/bam-readcount  
  
WORKDIR /opt/bam-readcount  
RUN git clone https://github.com/genome/bam-readcount.git /tmp/bam-
readcount-0.7.4 && \  
git -C /tmp/bam-readcount-0.7.4 checkout v0.7.4 && \  
cmake /tmp/bam-readcount-0.7.4 && \  
make && \  
rm -rf /tmp/bam-readcount-0.7.4 && \  
ln -s /opt/bam-readcount/bin/bam-readcount /usr/bin/bam-readcount  
  
COPY bam_readcount_helper.py /usr/bin/bam_readcount_helper.py  
COPY add_bam_readcount_to_vcf_helper.py
/usr/bin/add_bam_readcount_to_vcf_helper.py  
  
RUN pip install cyvcf2  
RUN pip3 install vcfpy  
  
##########  
#fpfilter#  
##########  
WORKDIR /opt  
RUN wget --no-check-certificate
https://raw.githubusercontent.com/genome/fpfilter-tool/v0.1.0/fpfilter.pl && \  
cp fpfilter.pl /usr/bin/fpfilter.pl && \  
rm fpfilter.pl  
  
#######  
#tabix#  
#######  
RUN ln -s $HTSLIB_INSTALL_DIR/bin/tabix /usr/bin/tabix  
  
######  
#docm#  
######  
COPY docm_filter.pl /usr/bin/docm_filter.pl  
COPY single_sample_docm_filter.pl /usr/bin/single_sample_docm_filter.pl  
  
########  
#VEP 90#  
########  
RUN mkdir /opt/vep/  
WORKDIR /opt/vep  
  
RUN git clone https://github.com/Ensembl/ensembl-vep.git  
WORKDIR /opt/vep/ensembl-vep  
RUN git checkout postreleasefix/90  
  
RUN perl INSTALL.pl --NO_UPDATE  
  
WORKDIR /  
RUN ln -s /opt/vep/ensembl-vep/vep /usr/bin/variant_effect_predictor.pl  
  
RUN mkdir -p /opt/lib/perl/VEP/Plugins  
COPY Downstream.pm /opt/lib/perl/VEP/Plugins/Downstream.pm  
COPY Wildtype.pm /opt/lib/perl/VEP/Plugins/Wildtype.pm  
  
COPY add_annotations_to_table_helper.py
/usr/bin/add_annotations_to_table_helper.py  
COPY docm_and_coding_indel_selection.pl
/usr/bin/docm_and_coding_indel_selection.pl  
  
################  
#bcftools 1.3.1#  
################  
ENV BCFTOOLS_INSTALL_DIR=/opt/bcftools  
  
WORKDIR /tmp  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2
&& \  
tar --bzip2 -xf bcftools-1.3.1.tar.bz2  
  
WORKDIR /tmp/bcftools-1.3.1  
RUN make prefix=$BCFTOOLS_INSTALL_DIR && \  
make prefix=$BCFTOOLS_INSTALL_DIR install  
  
WORKDIR /  
RUN rm -rf /tmp/bcftools-1.3.1  
  
###############  
#Picard 2.18.1#  
###############  
RUN mkdir /opt/picard-2.18.1/ \  
&& cd /tmp/ \  
&& wget --no-check-certificate
https://github.com/broadinstitute/picard/releases/download/2.18.1/picard.jar \  
&& mv picard.jar /opt/picard-2.18.1/ \  
&& ln -s /opt/picard-2.18.1 /opt/picard \  
&& ln -s /opt/picard-2.18.1 /usr/picard  
  
COPY split_interval_list_helper.pl /usr/bin/split_interval_list_helper.pl  
  
######  
#Toil#  
######  
RUN pip install toil[cwl]==3.12.0  
RUN cd /tmp/ \  
&& wget --no-check-certificate
https://raw.githubusercontent.com/tmooney/toil/3.12_lsf_fix/src/toil/batchSystems/lsfHelper.py
\  
&& mv -f lsfHelper.py /usr/local/lib/python2.7/dist-
packages/toil/batchSystems/ \  
&& wget --no-check-certificate
https://raw.githubusercontent.com/tmooney/toil/3.12_lsf_fix/src/toil/batchSystems/lsf.py
\  
&& mv -f lsf.py /usr/local/lib/python2.7/dist-packages/toil/batchSystems/  
RUN sed -i 's/select\\[type==X86_64 && mem/select[mem/'
/usr/local/lib/python2.7/dist-packages/toil/batchSystems/lsf.py  
  
RUN apt-get update -y && apt-get install -y libnss-sss tzdata  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime  
  
#LSF: Java bug that need to change the /etc/timezone.  
# The above /etc/localtime is not enough.  
RUN echo "America/Chicago" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
#############  
#verifyBamId#  
#############  
RUN apt-get update && apt-get install -y build-essential gcc-multilib apt-
utils zlib1g-dev git  
  
RUN cd /tmp/ && git clone https://github.com/statgen/verifyBamID.git && git
clone https://github.com/statgen/libStatGen.git  
  
RUN cd /tmp/libStatGen && git checkout tags/v1.0.14  
  
RUN cd /tmp/verifyBamID && git checkout tags/v1.1.3 && make  
  
RUN cp /tmp/verifyBamID/bin/verifyBamID /usr/local/bin  
  
RUN rm -rf /tmp/verifyBamID /tmp/libStatGen  
  
###  
#R#  
###  
RUN apt-get update && apt-get install -y r-base littler  
  
RUN apt-get install -y lib32ncurses5  
  
# Install R Packages  
RUN Rscript -e 'install.packages("ggplot2",
repos="http://cran.us.r-project.org", dependencies=TRUE)'  
  
###########  
#vcf_check#  
###########  
COPY vcf_check.pl /usr/bin/vcf_check.pl  
  
#############  
#fgbio 0.5.0#  
#############  
RUN wget --no-check-certificate
https://github.com/fulcrumgenomics/fgbio/releases/download/0.5.0/fgbio-0.5.0.jar
\  
&& mv fgbio-0.5.0.jar /opt  
  
###############  
#umi alignment#  
###############  
COPY umi_alignment.sh /usr/bin/umi_alignment.sh  
COPY umi_realignment.sh /usr/bin/umi_realignment.sh  

