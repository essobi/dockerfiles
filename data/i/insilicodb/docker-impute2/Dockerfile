# the base image to Ubuntu  
FROM ubuntu:16.04  
# Update the repository sources list and install samtools package  
RUN apt-get update  
RUN apt-get -y install libcurl4-gnutls-dev  
RUN apt-get -y install libcurl4-openssl-dev  
RUN apt-get -y install libxml2-dev \  
libssl-dev \  
r-base \  
r-base-dev \  
default-jdk \  
samtools \  
git \  
libboost-all-dev \  
wget \  
unzip \  
htop \  
sudo \  
tabix \  
curl \  
build-essential \  
python \  
python3 \  
python-pip \  
python3-pip  
  
RUN apt-get -y install bcftools vcftools  
  
#install java  
RUN apt-get -y install default-jre  
  
#install nextflow  
WORKDIR /usr/local/bin  
RUN curl -o nextflow -fsSL get.nextflow.io  
RUN chmod +x nextflow  
RUN /usr/local/bin/nextflow  
  
#install node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
#install awscli  
RUN pip install awscli --upgrade  
  
#install gsutil  
RUN pip install gsutil  
  
RUN mkdir /install  
  
WORKDIR /install  
# Get plink 1.9  
#install plink  
# RUN wget https://www.cog-
genomics.org/static/bin/plink170113/plink_linux_x86_64.zip  
COPY install/plink_linux_x86_64.zip .  
RUN unzip plink_linux_x86_64.zip -d plink-1.9  
RUN mv plink-1.9/plink plink-1.9/plink-1.9  
ENV PATH /install/plink-1.9:$PATH  
  
COPY install/plink_linux_x86_64_old_1.9.zip .  
RUN unzip plink_linux_x86_64_old_1.9.zip -d plink-1.9-old  
RUN mv plink-1.9-old/plink plink-1.9-old/plink-1.9-old  
ENV PATH /install/plink-1.9-old:$PATH  
  
#get plink 1.7  
# RUN wget https://www.cog-
genomics.org/static/bin/plink/plink1_linux_x86_64.zip  
COPY install/plink-1.07-x86_64.zip .  
RUN unzip plink-1.07-x86_64.zip -d plink-1.07  
RUN mv plink-1.07/plink-1.07-x86_64/plink
plink-1.07/plink-1.07-x86_64/plink-1.07  
ENV PATH /install/plink-1.07/plink-1.07-x86_64:$PATH  
  
#install shapeit  
# RUN wget
https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.v2.r837.GLIBCv2.12.Linux.static.tgz  
COPY install/shapeit.v2.r837.GLIBCv2.12.Linux.static.tgz .  
RUN tar -zxvf shapeit.v2.r837.GLIBCv2.12.Linux.static.tgz  
ENV PATH /install/bin:$PATH  
  
#install impute2  
# RUN wget
https://mathgen.stats.ox.ac.uk/impute/impute_v2.3.2_x86_64_static.tgz  
COPY install/impute_v2.3.2_x86_64_static.tgz .  
RUN tar -zxvf impute_v2.3.2_x86_64_static.tgz  
ENV PATH /install/impute_v2.3.2_x86_64_static:$PATH  
  
#Get gtools  
# RUN wget
http://www.well.ox.ac.uk/~cfreeman/software/gwas/gtool_v0.7.5_x86_64.tgz  
COPY install/gtool_v0.7.5_x86_64.tgz .  
RUN tar zxvf gtool_v0.7.5_x86_64.tgz  
  
COPY scripts /scripts  
WORKDIR /scripts/lab-files  
RUN npm install  
  
RUN mkdir /reference  
WORKDIR /reference  
COPY reference/23andme.snps.txt .  
  
RUN mkdir /workdir  
WORKDIR /workdir  
  
RUN Rscript -e "install.packages('jsonlite',
repos='http://cran.us.r-project.org')"  
#RUN Rscript -e "install.packages('openxlsx', dependencies=TRUE,
repos='http://ftp.heanet.ie/mirrors/cran.r-project.org/')"  
#RUN Rscript -e "install.packages('biomaRt',
repos='http://cran.us.r-project.org')"  
#R -e 'chooseCRANmirror(graphics=FALSE, ind=87);'  
COPY snp-imputation.nf .  
COPY snp-imputation-labfiles-preprocessing.nf .  
COPY gencove-processing.nf .  

