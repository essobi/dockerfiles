FROM ubuntu:14.04  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
RUN PERL_MM_USE_DEFAULT=1 apt-get update -q \  
&& apt-get dist-upgrade -qy \  
&& apt-get install -qyy openjdk-7-jre-headless perl-doc wget curl build-
essential git \  
&& cpan YAML Plack Plack::Handler::Starman Template JSON Getopt::Long
Data::Dumper LWP::UserAgent Test::More Dancer \  
&& cd /opt && git clone --branch v1.3.1 https://github.com/nmdp-
bioinformatics/service-ars \  
&& curl -OL http://search.maven.org/remotecontent?filepath=org/nmdp/ngs/ngs-
tools/1.8.3/ngs-tools-1.8.3.deb \  
&& dpkg --install ngs-tools-1.8.3.deb && rm ngs-tools-1.8.3.deb \  
&& export PATH=/opt/ngs-tools/bin:$PATH \  
&& cd service-ars/ARS_App && perl Makefile.PL \  
&& make && make test && make install  
  
ENV PATH /opt/ngs-tools/bin:$PATH  
  
VOLUME /opt/service-ars/ARS_App  
  
EXPOSE 8080  
EXPOSE 5050  
  
WORKDIR /opt/service-ars/ARS_App  
CMD plackup -E deployment -s Starman --workers=10 -p 5050 -a /opt/service-
ars/ARS_App/bin/app.pl  
  

