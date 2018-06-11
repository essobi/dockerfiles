FROM ubuntu:14.04  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
RUN PERL_MM_USE_DEFAULT=1 apt-get update -q \  
&& apt-get dist-upgrade -qy \  
&& apt-get install -qyy openjdk-7-jre-headless perl-doc wget curl build-
essential git \  
&& curl -OL http://search.maven.org/remotecontent?filepath=org/nmdp/ngs/ngs-
tools/1.8.3/ngs-tools-1.8.3.deb \  
&& dpkg --install ngs-tools-1.8.3.deb && rm ngs-tools-1.8.3.deb \  
&& cpan Getopt::Long Data::Dumper LWP::UserAgent Test::More HTML::TreeBuilder
\  
&& export PATH=/opt/ngs-tools/bin:$PATH \  
&& cd /opt && git clone --branch v1.4.0 https://github.com/nmdp-
bioinformatics/pipeline \  
&& cd /opt/pipeline/validation && perl Makefile.PL \  
&& make && make test && make install  
  
ENV PATH /opt/ngs-tools/bin:$PATH  
  
CMD ["/bin/bash"]  

