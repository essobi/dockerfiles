FROM ubuntu:14.04  
# maintainer  
MAINTAINER Krutika Gaonkar  
  
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
IO::Zlib  
  
RUN cpanm CPAN::Meta \  
Data::Dumper  
  
RUN cpanm CPAN::Meta \  
Getopt::Long  
  
WORKDIR /opt  
  
#add scripts  
ADD filter_criteria.sh /opt/filter_criteria.sh  

