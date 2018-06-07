FROM ubuntu:12.04  
MAINTAINER Zaahir Moolla <moollaza@duckduckgo.com>  
  
# Perlbrew Setup borrowed from  
# https://github.com/RsrchBoy/perlbrew-base-dock/blob/master/Dockerfile  
# Update packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu precise main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E1DD270288B4E6030699E45FA1715D88E1DF1F24  
RUN apt-get update && apt-get -y install git curl build-essential perl ruby  
  
# Prep for the install...  
RUN umask 0022  
RUN mkdir -p /usr/local/perlbrew /root  
ENV HOME /root  
ENV PERLBREW_ROOT /usr/local/perlbrew  
ENV PERLBREW_HOME /root/.perlbrew  
  
# Install Perlbrew and cpanm  
RUN curl -kL http://install.perlbrew.pl | bash  
ENV PATH /usr/local/perlbrew/bin:$PATH  
ENV PERLBREW_PATH /usr/local/perlbrew/bin  
RUN perlbrew install-cpanm  
RUN perlbrew info  
  
# Set desired Perl  
ENV TARGET_PERL_FULL 5.16.3  
ENV TARGET_PERL 5.16  
# Install Perl  
RUN perlbrew download $TARGET_PERL_FULL  
RUN perlbrew install -j4 --as $TARGET_PERL $TARGET_PERL_FULL  
RUN rm -rf /usr/local/perlbrew/build/*  
  
RUN perlbrew switch $TARGET_PERL  
  
ENV PATH /usr/local/perlbrew/perls/$TARGET_PERL/bin:$PATH  
ENV MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_PATH
/usr/local/perlbrew/bin:/usr/local/perlbrew/perls/$TARGET_PERL/bin  
ENV PERLBREW_PERL $TARGET_PERL  
  
RUN perlbrew info  
RUN perl -v  
  
# Install DuckPAN  
RUN apt-get install -y libssl-dev  
RUN cpanm -n App::DuckPAN  
  
# Install DDG  
RUN duckpan DDG  

