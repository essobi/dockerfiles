FROM debian:jessie  
  
LABEL name="LIGO Base Debian Jessie - Proposed" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20170606" \  
support="Reference Platform"  
  
# ensure non-interactive debian installation  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# support https repositories  
RUN apt-get update && apt-get --assume-yes install apt-transport-https  
  
# Add required repositories  
RUN echo "deb http://research.cs.wisc.edu/htcondor/debian/stable jessie
contrib" > /etc/apt/sources.list.d/condor.list  
RUN echo "deb http://software.ligo.org/gridtools/debian jessie main" >
/etc/apt/sources.list.d/gridtools.list  
RUN echo "deb http://software.ligo.org/lscsoft/debian jessie contrib" >
/etc/apt/sources.list.d/lscsoft.list  
RUN echo "deb http://software.ligo.org/lscsoft/debian jessie-proposed contrib"
> /etc/apt/sources.list.d/lscsoft-proposed.list  
RUN echo "deb https://packagecloud.io/github/git-lfs/debian jessie main" >
/etc/apt/sources.list.d/git-lfs.list  
  
# add LIGO, HTCondor, and git-lfs signing keys  
RUN apt-key adv --keyserver pgp.mit.edu --recv-key
8325FECB83821E31D3582A69CE050D236DB6FA3F  
RUN apt-key adv --keyserver pgp.mit.edu --recv-key
4B9D355DF3674E0E272D2E0A973FC7D2670079F6  
RUN apt-key adv --keyserver pgp.mit.edu --recv-key
418A7F2FB0E1E6E7EABF6FE8C2E73424D59097AB  
  
# Setup a working bash shell  
RUN apt-get update && apt-get --assume-yes install apt-utils bash-completion
&& \  
rm -rf /var/lib/apt/lists/*  

