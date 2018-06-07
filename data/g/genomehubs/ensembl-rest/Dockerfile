# DOCKER-VERSION 1.12.3  
FROM ubuntu:16.04  
MAINTAINER Sujai Kumar/Lepbase contact@lepbase.org  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y apt-utils  
RUN apt-get install -y nano wget  
  
RUN echo 'deb http://gb.archive.ubuntu.com/ubuntu/ xenial-updates main
restricted' >> /etc/apt/sources.list  
RUN echo 'deb http://gb.archive.ubuntu.com/ubuntu/ xenial-updates universe' >>
/etc/apt/sources.list  
RUN echo 'deb http://gb.archive.ubuntu.com/ubuntu/ xenial-updates multiverse'
>> /etc/apt/sources.list  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y git vim libxml2-dev cpanminus libxml-libxml-perl
libxml-simple-perl \  
libxml-writer-perl libdbi-perl libdbd-mysql-perl build-essential libtest-
differences-perl \  
libtest-json-perl libtest-xml-simple-perl zlib1g-dev htslib-test libhts-dev
libhts1 libtabixpp-dev \  
tabix samtools \  
libbz2-dev libbz2-1.0 liblzma-dev  
  
RUN apt-get install -y wget  
RUN wget
https://github.com/samtools/htslib/releases/download/1.4/htslib-1.4.tar.bz2  
RUN tar xf htslib-1.4.tar.bz2  
WORKDIR htslib-1.4  
RUN make install  
  
RUN apt-get clean  
  
RUN cpanm Module::Install Catalyst Catalyst::Devel Hash::Merge
Catalyst::Plugin::ConfigLoader \  
Catalyst::Plugin::Static::Simple Catalyst::Plugin::Session::Store::FastMmap \  
Catalyst::Component::InstancePerContext Catalyst::View::JSON
Log::Log4perl::Catalyst \  
Catalyst::Plugin::Cache Parse::RecDescent Catalyst::Controller::REST
Catalyst::View::TT \  
Catalyst::Plugin::Authentication Catalyst::Plugin::Cache
Catalyst::Action::RenderView \  
CHI CHI::Driver::Memcached::Fast \  
Test::XPath Test::XML::Simple \  
Devel::Peek Devel::Cycle Error IO::String PadWalker Test::Builder::Module  
  
ENV home /home/ubuntu  
ENV user ubuntu  
ENV ENSEMBL_VERSION 85  
RUN mkdir -p $home/programs  
WORKDIR $home/programs  
RUN git clone https://github.com/Ensembl/ensembl-git-tools.git  
WORKDIR $home  
  
RUN mkdir -p $home/src  
WORKDIR $home/src  
RUN wget https://github.com/bioperl/bioperl-live/archive/bioperl-
release-1-6-9.tar.gz  
RUN tar zxf bioperl-release-1-6-9.tar.gz  
RUN mv bioperl-live-bioperl-release-1-6-9 bioperl-1.6.9  
  
WORKDIR $home/src  
RUN $home/programs/ensembl-git-tools/bin/git-ensembl --clone rest ensembl-test  
RUN $home/programs/ensembl-git-tools/bin/git-ensembl --checkout --branch
"release/$ENSEMBL_VERSION" rest ensembl-test  
  
RUN export PERL5LIB=/home/ubuntu/src/bioperl-1.6.9/  
RUN cpanm Bio::DB::HTS  
  
#RUN wget -O /home/ubuntu/.profile
https://raw.githubusercontent.com/andrewyatz/vagrant_machines/master/ensembl/rest/settings/profile  
RUN perl -i -plne 's/use Catalyst qw\//use Catalyst qw\/\n
-Debug\nSession::Store::FastMmap/' $home/src/ensembl-rest/lib/EnsEMBL/REST.pm  
RUN adduser --disabled-password --gecos '' $user  
RUN chown -R $user:$user $home  
  
EXPOSE 80  
USER ubuntu  
env PATH /home/ubuntu/programs/ensembl-git-tools/bin:$PATH  
  
# Set up PERL5LIB  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/bioperl-1.6.9  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl/modules  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl-compara/modules  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl-variation/modules  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl-funcgen/modules  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl-test/modules  
ENV PERL5LIB $PERL5LIB:/home/ubuntu/src/ensembl-io/modules  
ENV PERL5LIB=$PERL5LIB:/home/ubuntu/src/tabix-
master/perl/blib/lib:/home/ubuntu/src/tabix-master/perl/blib/arch  
ENV LD_LIBRARY_PATH=/home/ubuntu/src/tabix-master/  
  
USER root  
CMD ["/home/ubuntu/src/ensembl-rest/script/ensembl_rest_server.pl","-p","80"]  

