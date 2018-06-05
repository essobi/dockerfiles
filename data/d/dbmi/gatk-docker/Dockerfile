## Docker source file for image duplexa/gatk_env:v1 on hub.docker.com.  
FROM centos:7  
MAINTAINER Soo Lee  
  
## installing basic packages  
RUN yum update -y && yum install -y wget gcc make gcc-c++ epel-release ##
wget,gcc,make,gcc-c=+,epel-release are necessary for R  
## installing R 3.1.2 ##  
WORKDIR /usr/local/bin/  
#RUN wget http://lib.stat.cmu.edu/R/CRAN/src/base/R-3/R-3.1.2.tar.gz && tar
xzvf R-3.1.2.tar.gz # downloading R 3.1.2  
#WORKDIR /usr/local/bin/R-3.1.2  
#RUN yum-builddep R -y ## installing necessary dependencies for R  
#RUN ./configure && make && make install && make install-info && make install-
pdf ## installing R 3.1.2  
## End Installing R 3.1.2 ##  
## The rest is copied  
WORKDIR /usr/local/bin/  
COPY annovar/ annovar/  
COPY BEDtools-2.23.0/ BEDtools-2.23.0/  
COPY bincov/ bincov/  
COPY bwa-0.7.8/ bwa-0.7.8/  
COPY fastqc-0.11.3/ fastqc-0.11.3/  
COPY GATK3.4/ GATK3.4/  
COPY GATK3.5/ GATK3.5/  
COPY GATK3.5n/ GATK3.5n/  
COPY GATK3.6/ GATK3.6/  
COPY jdk1.7.0_71/ jdk1.7.0_71/  
COPY mutect/ mutect/  
COPY picard-1.130/ picard-1.130/  
COPY samtools-1.3/ samtools-1.3/  
COPY tabix-0.2.6/ tabix-0.2.6/  
COPY VarScan/ VarScan/  
COPY vcftools-0.1.12/ vcftools-0.1.12/  
## java1.8 needed for GATK3.6  
COPY jdk1.8.0_45/ jdk1.8.0_45/  
COPY jdk1.6.0_45/ jdk1.6.0_45/  
COPY run_scripts/ run_scripts/  
COPY run_scripts2/ run_scripts2/  
  
## path  
ENV PATH
/usr/local/bin/run_scripts2/:/usr/local/bin/run_scripts/:/usr/local/bin/annovar/:/usr/local/bin/BEDtools-2.23.0/bin/:/usr/local/bin/bincov/:/usr/local/bin/bwa-0.7.8/bin/:/usr/local/bin/fastqc-0.11.3/:/usr/local/bin/jdk1.7.0_71/bin/:/usr/local/bin/samtools-1.3/bin/:/usr/local/bin/tabix-0.2.6/:/usr/local/bin/vcftools-0.1.12/bin/:$PATH  
## by default Java 1.7 is included in the path. To use Java 1.8,
/usr/local/bin/jdk1.8.0_45/bin/ must be included in the path in run time.  
## default command is bash.  
CMD ['bash']  
  

