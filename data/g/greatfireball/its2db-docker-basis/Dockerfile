# This file can be used to create a docker container based on Ubuntu  
# for the ITS2 database  
  
FROM ubuntu:latest  
MAINTAINER Frank Förster <frank.foerster@biozentrum.uni-wuerzburg.de>  
  
  
# Install packages from first installation step  
RUN apt-get update && apt-get install --quiet --assume-yes \  
build-essential \  
bzip2 \  
fonts-liberation \  
gcc \  
git \  
libapache2-mod-fcgid \  
libapache2-mod-php5 \  
libdbd-pg-perl \  
libgd3 \  
libjson-xs-perl \  
librsvg2-bin \  
libxml-perl \  
libxml-libxml-perl \  
make \  
subversion \  
tar \  
zip  
  
# install required perl modules  
RUN for MODULE in \  
WWW::Mechanize \  
Test::WWW::Mechanize \  
DBIx::Class::Schema::Loader \  
XML::LibXML \  
Bio::SearchIO \  
Class::MOP \  
YAML::XS \  
Hash::Merge \  
FCGI \  
FCGI::ProcManager \  
Switch \  
String::Random \  
DBD::SQLite \  
DBD::Pg \  
DBICx::Deploy \  
DBIx::Class \  
DBIx::Class::Tree \  
DateTime \  
DateTime::Format::Pg \  
XML::Simple \  
Catalyst::Devel \  
Catalyst::Helper::View::TT \  
Catalyst::View::JSON \  
Catalyst::View::Download \  
Catalyst::Plugin::Session \  
Catalyst::Plugin::Session::Store::FastMmap \  
Catalyst::Plugin::Session::State::Cookie \  
Catalyst::Model::DBIC::Schema \  
Catalyst::Controller::BindLex \  
Catalyst::Controller::REST; \  
do perl -MCPAN -e "install $MODULE"; done  
  
# Adding the required packages to add PPAs:  
RUN apt-get install --assume-yes software-properties-common  
  
# And enable the multiverse repository  
RUN apt-add-repository multiverse && apt-get update  
  
# Adding the PPA for the viennarna package  
RUN add-apt-repository --yes ppa:j-4/vienna-rna  
  
# And install the vienna-rna package  
RUN apt-get update && apt-get install --quiet --assume-yes vienna-rna  
  
# Install the package imagemagick  
RUN apt-get install --quiet --assume-yes imagemagick  
  
# Install the ncbi-blast+ package  
RUN apt-get install --quiet --assume-yes ncbi-blast+  
  
# Install the emboss package  
RUN apt-get install --quiet --assume-yes emboss  
  
# Install the muscle package  
RUN apt-get install --quiet --assume-yes muscle  
  
# Install the clustalw package  
RUN apt-get install --quiet --assume-yes clustalw  
  
# Install the hmmer2 package  
RUN apt-get install --quiet --assume-yes hmmer2  
  
# Install everything which is required for newick_utils  
RUN apt-get install --quiet --assume-yes bison  
RUN apt-get install --quiet --assume-yes flex  
RUN apt-get install --quiet --assume-yes sudo autoconf libtool  
  
# Clone the repository and install  
RUN cd /tmp/ && \  
git clone https://github.com/tjunier/newick_utils.git && \  
cd newick_utils && \  
autoreconf -fi && \  
./configure && \  
make && \  
make check && \  
make install  

