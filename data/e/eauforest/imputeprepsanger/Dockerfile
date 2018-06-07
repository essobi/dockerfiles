FROM centos  
  
MAINTAINER Marie Forest <marie.forest@ladydavis.ca>  
MAINTAINER Natacha Beck <natacha.beck@mcgill.ca>  
  
# Install prerequisite  
RUN yum update -y  
  
# Install basic packages  
RUN yum install -y bzip2 \  
gcc \  
git \  
make \  
perl \  
unzip \  
wget \  
zlib-devel \  
which  
  
COPY . imputePrepSanger  
  
WORKDIR /imputePrepSanger/  
  
# INSTALL TOOLS  
# 1. Tools that come with this pipeline  
RUN chmod 755 /imputePrepSanger/imputePrep_script.sh \  
&& cp /imputePrepSanger/imputePrep_script.sh /bin/  
  
RUN chmod 755 /imputePrepSanger/HRC-1000G-check-bim_modified.pl \  
&& cp /imputePrepSanger/HRC-1000G-check-bim_modified.pl /bin/  
  
RUN chmod 755 /imputePrepSanger/update_build.sh \  
&& cp /imputePrepSanger/update_build.sh /bin/  
  
RUN chmod 755 /imputePrepSanger/reportRedaction.sh \  
&& cp /imputePrepSanger/reportRedaction.sh /bin/  
  
# 2. External tools  
# a. bcftools  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2
\  
&& bunzip2 -f bcftools-1.3.1.tar.bz2 \  
&& tar -xvf bcftools-1.3.1.tar \  
&& cd bcftools-1.3.1 \  
&& make \  
&& make install  
  
RUN cp bcftools-1.3.1/bcftools /bin/  
  
# b. plink  
#RUN wget
http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-1.07-x86_64.zip \  
# && unzip plink-1.07-x86_64.zip  
#RUN cp plink-1.07-x86_64/plink /bin/  
RUN unzip plink_linux_x86_64.zip -d ./plink  
  
RUN cp plink/plink /bin/  
  

