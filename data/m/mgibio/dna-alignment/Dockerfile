FROM ubuntu:xenial  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
description="Image for tools used in alignment"  
  
RUN apt-get update -y && apt-get install -y \  
ant \  
apt-utils \  
build-essential \  
bzip2 \  
default-jdk \  
default-jre \  
gcc-multilib \  
git \  
libncurses5-dev \  
libnss-sss \  
nodejs \  
python-dev \  
python-pip \  
r-base \  
tzdata \  
unzip \  
wget \  
zlib1g-dev  
  
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
#Picard 2.18.1#  
###############  
  
RUN mkdir /opt/picard-2.18.1/ \  
&& cd /tmp/ \  
&& wget --no-check-certificate
https://github.com/broadinstitute/picard/releases/download/2.18.1/picard.jar \  
&& mv picard.jar /opt/picard-2.18.1/ \  
&& ln -s /opt/picard-2.18.1 /opt/picard  
  
#############  
#fgbio 0.5.0#  
#############  
RUN wget --no-check-certificate
https://github.com/fulcrumgenomics/fgbio/releases/download/0.5.0/fgbio-0.5.0.jar
\  
&& mv fgbio-0.5.0.jar /opt  
  
######  
#Toil#  
######  
RUN pip install --upgrade pip \  
&& hash -r pip \  
&& pip install toil[cwl]==3.12.0 \  
&& cd /tmp/ \  
&& wget --no-check-certificate
https://raw.githubusercontent.com/tmooney/toil/3.12_lsf_fix/src/toil/batchSystems/lsfHelper.py
\  
&& mv -f lsfHelper.py /usr/local/lib/python2.7/dist-
packages/toil/batchSystems/ \  
&& wget --no-check-certificate
https://raw.githubusercontent.com/tmooney/toil/3.12_lsf_fix/src/toil/batchSystems/lsf.py
\  
&& mv -f lsf.py /usr/local/lib/python2.7/dist-packages/toil/batchSystems/ \  
&& sed -i 's/select\\[type==X86_64 && mem/select[mem/'
/usr/local/lib/python2.7/dist-packages/toil/batchSystems/lsf.py  
  
# Install R Packages  
RUN Rscript -e 'install.packages("ggplot2",
repos="http://cran.us.r-project.org", dependencies=TRUE)'  
  
# Define a timezone so Java works properly  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime \  
&& echo "America/Chicago" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
# helper scripts  
COPY alignment_helper.sh /usr/bin/alignment_helper.sh  
COPY markduplicates_helper.sh /usr/bin/markduplicates_helper.sh  
COPY umi_alignment.sh /usr/bin/umi_alignment.sh  
COPY umi_realignment.sh /usr/bin/umi_realignment.sh  

