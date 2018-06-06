FROM ubuntu:xenial  
MAINTAINER Susanna Kiwala <ssiebert@wustl.edu>  
  
LABEL \  
description="Image for tools used in the CLE"  
  
RUN apt-get update -y && apt-get install -y \  
wget \  
git \  
unzip \  
bzip2 \  
g++ \  
make \  
zlib1g-dev \  
ncurses-dev \  
perl-doc \  
python \  
rsync \  
default-jdk \  
default-jre \  
bioperl \  
libfile-copy-recursive-perl \  
libarchive-extract-perl \  
libarchive-zip-perl \  
libapache-dbi-perl \  
curl \  
ant  
  
RUN apt-get update -y && apt-get install -y python-pip python-dev build-
essential nodejs  
RUN pip install --upgrade pip  
  
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
&& git clone --recursive https://github.com/broadgsa/gatk-protected.git \  
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
--prefix=$SAMTOOLS_INSTALL_DIR && \  
make && \  
make install  
  
WORKDIR /  
RUN rm -rf /tmp/samtools-1.3.1  
  
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
  
RUN pip install cyvcf2  
  
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
  
########  
#VEP 86#  
########  
RUN mkdir /opt/vep/  
  
WORKDIR /opt/vep  
RUN wget https://github.com/Ensembl/ensembl-tools/archive/release/86.zip && \  
unzip 86.zip  
  
WORKDIR /opt/vep/ensembl-tools-release-86/scripts/variant_effect_predictor/  
RUN perl INSTALL.pl --NO_HTSLIB  
  
WORKDIR /  
RUN ln -s /opt/vep/ensembl-tools-
release-86/scripts/variant_effect_predictor/variant_effect_predictor.pl
/usr/bin/variant_effect_predictor.pl  
  
RUN mkdir -p /opt/lib/perl/VEP/Plugins  
COPY Downstream.pm /opt/lib/perl/VEP/Plugins/Downstream.pm  
COPY Wildtype.pm /opt/lib/perl/VEP/Plugins/Wildtype.pm  
  
COPY add_annotations_to_table_helper.py
/usr/bin/add_annotations_to_table_helper.py  
  
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
  
##############  
#Picard 2.4.1#  
##############  
ENV picard_version 2.4.1  
  
# Install ant, git for building  
  
# Assumes Dockerfile lives in root of the git repo. Pull source files into  
# container  
RUN cd /usr/ && git config --global http.sslVerify false && git clone
--recursive https://github.com/broadinstitute/picard.git && cd /usr/picard &&
git checkout tags/${picard_version}  
WORKDIR /usr/picard  
  
# Clone out htsjdk. First turn off git ssl verification  
RUN git config --global http.sslVerify false && git clone
https://github.com/samtools/htsjdk.git && cd htsjdk && git checkout
tags/${picard_version} && cd ..  
  
# Build the distribution jar, clean up everything else  
RUN ant clean all && \  
mv dist/picard.jar picard.jar && \  
mv src/scripts/picard/docker_helper.sh docker_helper.sh && \  
ant clean && \  
rm -rf htsjdk && \  
rm -rf src && \  
rm -rf lib && \  
rm build.xml  
  
COPY split_interval_list_helper.pl /usr/bin/split_interval_list_helper.pl  
  
######  
#Toil#  
######  
RUN pip install toil[cwl]==3.6.0  
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
  
#############  
#Concordance#  
#############  
ENV CONCORDANCE_INSTALL_DIR=/opt/concordance  
  
WORKDIR $CONCORDANCE_INSTALL_DIR  
RUN wget
https://raw.githubusercontent.com/mnneveau/concordance/master/newConcordance.py  
  
RUN pip install FisherExact  

