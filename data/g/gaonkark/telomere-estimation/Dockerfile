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
  
WORKDIR /opt  
  
#add scripts  
ADD terra_finder.pl /opt/terra_finder.pl  
  

