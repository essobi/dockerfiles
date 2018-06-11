FROM mcfonsecalab/python36_bio  
  
MAINTAINER Pedro Barbosa <pedro.barbosa@medicina.ulisboa.pt>  
  
WORKDIR /tools  
  
RUN apt-get update && \  
apt-get install -y git gcc g++ make zlib1g-dev bzip2 libbz2-1.0 libbz2-dev
libbz2-ocaml libbz2-ocaml-dev liblzma-dev unzip  
  
#SNPEFF & SNPSIFT  
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle"  
LABEL description="java8"  
RUN apt-get install -y --no-install-recommends locales && \  
locale-gen en_US.UTF-8 && \  
apt-get dist-upgrade -y && \  
apt-get --purge remove openjdk* && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
apt-get install -y --no-install-recommends oracle-java8-installer oracle-
java8-set-default  
  
LABEL snpeff="version 4.3"  
ADD https://downloads.sourceforge.net/project/snpeff/snpEff_latest_core.zip
/tools/  
RUN unzip snpEff_latest_core.zip && rm snpEff_latest_core.zip  
  
ENV SNPEFF_HOME="/tools/snpEff"  
#Download hg19 and hg38 genome versions  
RUN java -jar $SNPEFF_HOME/snpEff.jar download GRCh37.75  
RUN java -jar $SNPEFF_HOME/snpEff.jar download GRCh38.86  
  
#BCFTOOLS  
LABEL bcftools="version 1.7-1-ge07034a (using htslib 1.7-22-gf9e5e35)"  
RUN git clone git://github.com/samtools/htslib.git && git clone
git://github.com/samtools/bcftools.git && cd bcftools && make  
ENV PATH="$PATH:/tools/bcftools"  
#Update conda, if new version is available  
#RUN conda update -n base conda  
#Vt  
LABEL Vt=""  
RUN conda install -c bioconda vt && conda update vt  
  
#VCFANNO  
LABEL vcfanno="version 0.2.8"  
RUN conda install -c bioconda vcfanno  
  
#PYVCF  
LABEL pyvcf="0.6.8"  
RUN conda install -c bioconda pyvcf  
  
#scikit-allel  
LABEL scikit-allel="1.1.10"  
RUN conda install -c conda-forge scikit-allel  
  
#cyvc2  
LABEL cyvcf2="0.8.8"  
RUN pip install --upgrade pip && pip install cython && pip install cyvcf2  
#RUN git clone https://github.com/brentp/cyvcf2 && cd cyvcf2 && pip install
--editable .  
#install pybedtools  
RUN conda install -c bioconda pybedtools  
  
RUN apt-get remove git -y  
RUN apt-get clean all -y  
  

