FROM ubuntu:16.04  
MAINTAINER Jason L Weirather  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
make \  
g++ \  
gcc \  
build-essential \  
zlib1g-dev \  
libgsl0-dev \  
perl \  
curl \  
git \  
wget \  
unzip \  
tabix \  
libncurses5-dev  
  
RUN apt-get install -y cpanminus  
RUN apt-get install -y libmysqlclient-dev  
RUN cpanm CPAN::Meta \  
Archive::Zip \  
DBI \  
DBD::mysql \  
JSON \  
DBD::SQLite \  
Set::IntervalTree \  
LWP \  
LWP::Simple  
RUN cpanm Archive::Extract \  
Archive::Tar \  
Archive::Zip \  
CGI \  
Time::HiRes \  
Encode  
RUN cpanm --force File::Copy::Recursive  
RUN cpanm \  
Perl::OSType \  
Module::Metadata version \  
Bio::Root::Version \  
TAP::Harness \  
Module::Build  
  
WORKDIR /opt  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2  
RUN tar jxf samtools-1.3.tar.bz2  
WORKDIR /opt/samtools-1.3  
RUN make  
RUN make install  
  
WORKDIR /opt  
RUN rm samtools-1.3.tar.bz2  
  
WORKDIR /opt  
RUN wget https://github.com/jason-weirather/vcf2maf/archive/v1.6.16.tar.gz &&
\  
tar -xzf v1.6.16.tar.gz && \  
rm v1.6.16.tar.gz && \  
mv vcf2maf-1.6.16 vcf2maf  
  

