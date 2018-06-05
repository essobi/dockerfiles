FROM avastsoftware/cpanm  
  
MAINTAINER Avast Viruslab Systems  
  
RUN cpanm Minilla  
RUN yum install -y git  
  
#minilla release tests dependency  
RUN cpanm Test::CPAN::Meta Test::Pod Test::PAUSE::Permissions Test::Spellunker
Test::MinimumVersion::Fast  
  
VOLUME ["/tmp/minilla"]  
WORKDIR "/tmp/minilla"  

