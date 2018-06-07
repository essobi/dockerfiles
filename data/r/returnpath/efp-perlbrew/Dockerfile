FROM centos:7  
ENV USE_PERL 5.18.2  
ENV PERLBREW_ROOT /opt/perl5  
  
RUN yum -y install epel-release; yum -y install perl bzip2 patch unzip wget
make gcc postgresql postgresql-devel  
RUN curl -L http://install.perlbrew.pl | bash  
RUN source $PERLBREW_ROOT/etc/bashrc && \  
perlbrew install-cpanm && \  
perlbrew install $USE_PERL  
RUN source $PERLBREW_ROOT/etc/bashrc && \  
perlbrew use $USE_PERL && \  
cpanm install local::lib && \  
cpanm install FindBin  
  

