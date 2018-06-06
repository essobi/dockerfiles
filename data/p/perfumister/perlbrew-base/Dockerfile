# Ubuntu 16.04 LTS with Perlbrew, Perl, App::cpanminus & Carton  
FROM ubuntu:xenial  
MAINTAINER Perfumister <hey@perfumister.com>  
  
# Update and install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y \  
apt-utils build-essential locales git curl perl  
RUN locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
# Install perlbrew  
RUN umask 0022  
RUN mkdir -p /usr/local/perlbrew /root  
ENV HOME=/root \  
PERLBREW_ROOT=/usr/local/perlbrew \  
PERLBREW_HOME=$HOME/.perlbrew \  
PATH=/usr/local/perlbrew/bin:$PATH \  
PERLBREW_PATH=/usr/local/perlbrew/bin  
RUN curl -kL http://install.perlbrew.pl | bash  
  
# Install and use latest stable Perl  
RUN perlbrew install-cpanm && \  
perlbrew -n -j 4 install perl-5.18.4 --as current && \  
perlbrew use current && \  
echo "source /usr/local/perlbrew/etc/bashrc && perlbrew switch current" >>
$HOME/.bashrc  
  
# Install any other Perl modules  
RUN cpanm -q Carton  
  
# Clean up!  
RUN rm -rf /root/.cpanm  
RUN apt-get autoclean && \  
perlbrew clean && \  
perlbrew info && \  
exit  

