FROM ubuntu:trusty  
MAINTAINER Stephen Thirlwall <sdt@dr.com>  
  
# Following the instructions from:  
# http://blogs.perl.org/users/ovid/2015/03/tiny-games-with-perl-6.html  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
gcc \  
git \  
make && \  
git clone \--depth 1 https://github.com/tadzik/rakudobrew ~/.rakudobrew && \  
PATH=~/.rakudobrew/bin:$PATH rakudobrew build moar && \  
PATH=~/.rakudobrew/bin:$PATH rakudobrew build-panda && \  
echo ok.  
  
ENV PATH="/root/.rakudobrew/bin:$PATH"  
WORKDIR /run  

