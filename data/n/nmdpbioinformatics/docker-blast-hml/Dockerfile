FROM ubuntu:14.04  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
WORKDIR /blast  
  
COPY ngs-tools_1.9.deb /blast/ngs-tools_1.9.deb  
COPY ld-tools_0.1.deb /blast/ld-tools_0.1.deb  
  
RUN PERL_MM_USE_DEFAULT=1 apt-get update -q \  
&& apt-get dist-upgrade -qy \  
&& apt-get install -qyy openjdk-7-jre-headless perl-doc wget curl build-
essential git \  
&& dpkg --install /blast/ngs-tools_1.9.deb \  
&& dpkg --install /blast/ld-tools_0.1.deb \  
&& curl -O ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-
blast-2.3.0+-x64-linux.tar.gz \  
&& tar -xvzf ncbi-blast-2.3.0+-x64-linux.tar.gz && cp ncbi-blast-2.3.0+/bin/*
/opt/ngs-tools/bin \  
&& rm ncbi-blast-2.3.0+-x64-linux.tar.gz \  
&& cpan Getopt::Long Data::Dumper LWP::UserAgent Test::More HTML::TreeBuilder
\  
&& export PATH=/opt/ld-tools/bin:/opt/ngs-tools/bin:$PATH \  
&& cd /opt && git clone --branch v1.4.0 https://github.com/nmdp-
bioinformatics/pipeline \  
&& cd /opt/pipeline/validation && perl Makefile.PL \  
&& make && make test && make install \  
&& mkdir /opt/imgt && ngs-imgt-db -o /opt/imgt -c -r  
  
ENV PATH /opt/ngs-tools/bin:/opt/ld-tools/bin:$PATH  
  
CMD ["/bin/bash"]

