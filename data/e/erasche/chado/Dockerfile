FROM postgres:9.5  
  
ENV DEBIAN_FRONTEND=noninteractive \  
CHADO_DB_NAME=postgres \  
CHADO_DB_HOST=localhost \  
CHADO_DB_PORT=5432 \  
CHADO_DB_USERNAME=postgres \  
CHADO_DB_PASSWORD=postgres \  
POSTGRES_PASSWORD=postgres \  
GMOD_ROOT=/usr/share/gmod/ \  
PGDATA=/var/lib/postgresql/data/ \  
SCHEMA_URL=https://github.com/erasche/chado-schema-
builder/releases/download/1.31-jenkins110/chado-1.31.sql.gz \  
INSTALL_CHADO_SCHEMA=1 \  
INSTALL_YEAST_DATA=0  
  
# TODO: Pulled from webapollo docker image, some of these may be extraneous (I  
# think the heap stuff.) Installed most from apt for ease of installation  
RUN apt-get -qq update && \  
apt-get install --no-install-recommends -y build-essential \  
libpng-dev zlib1g zlib1g-dev build-essential make libpq-dev libperlio-gzip-
perl \  
libcapture-tiny-perl libtest-differences-perl libperlio-gzip-perl \  
libdevel-size-perl libdbi-perl libjson-perl libjson-xs-perl libheap-perl \  
libhash-merge-perl libdbd-pg-perl libio-string-perl libtest-most-perl \  
libarray-compare-perl libconvert-binary-c-perl libgraph-perl \  
libgraphviz-perl libsoap-lite-perl libsvg-perl libsvg-graph-perl \  
libset-scalar-perl libsort-naturally-perl libxml-sax-perl libxml-twig-perl \  
libxml-writer-perl libyaml-perl libgd2-xpm-dev curl xsltproc netcat wget perl-
doc \  
ca-certificates && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# Some have to be forced.  
# But most install just fine  
RUN mkdir -p $GMOD_ROOT $PGDATA && \  
curl -L http://cpanmin.us | perl \- App::cpanminus && \  
cpanm --force --notest Test::More Heap::Simple Heap::Simple::XS DBIx::DBStag
GO::Parser && \  
cpanm --notest DBI Digest::Crc32 Cache::Ref::FIFO URI::Escape HTML::Entities \  
HTML::HeadParser HTML::TableExtract HTTP::Request::Common LWP XML::Parser \  
XML::Parser::PerlSAX XML::SAX::Writer XML::Simple Data::Stag \  
Error PostScript::TextBlock Spreadsheet::ParseExcel Algorithm::Munkres \  
CJFIELDS/BioPerl-1.6.924.tar.gz Bio::GFF3::LowLevel::Parser File::Next CGI
DBD::Pg SQL::Translator \  
Digest::MD5 Text::Shellwords Module::Build Class::DBI Class::DBI::Pg \  
Class::DBI::Pager Template Bio::Chado::Schema GD GO::Parser Bio::FeatureIO \  
&& wget https://github.com/GMOD/Chado/archive/master.tar.gz -O
/tmp/master.tar.gz \  
&& cd / && tar xvfz /tmp/master.tar.gz \  
&& mv /Chado-master /chado \  
&& rm -f /tmp/master.tar.gz  
  
WORKDIR /chado/chado/  
# https://github.com/docker-
library/postgres/blob/a82c28e1c407ef5ddfc2a6014dac87bcc4955a26/9.4/docker-
entrypoint.sh#L85  
# This will cause the chado schema to load on boot and be MUCH better behaved.  
RUN perl Makefile.PL GMOD_ROOT=/usr/share/gmod/ DEFAULTS=1 RECONFIGURE=1 && \  
make && \  
make install && \  
wget --quiet $SCHEMA_URL -O /chado.sql.gz && gunzip /chado.sql.gz && \  
wget --quiet
http://downloads.yeastgenome.org/curation/chromosomal_feature/saccharomyces_cerevisiae.gff
&& \  
sed -i s'/%20/ /g' saccharomyces_cerevisiae.gff && \  
chown -R postgres:postgres /chado/chado/  
  
COPY load_schema.sh /docker-entrypoint-initdb.d/00-load_schema.sh  
COPY load_yeast.sh /docker-entrypoint-initdb.d/01-load_yeast.sh  
COPY search.sh /docker-entrypoint-initdb.d/02-search.sh  
COPY search.sql /search.sql  

