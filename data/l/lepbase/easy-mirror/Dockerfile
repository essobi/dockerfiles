# DOCKER-VERSION 1.12.3  
FROM debian:jessie  
MAINTAINER Richard Challis/Lepbase contact@lepbase.org  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y lsb-release apt-utils  
  
RUN sed -i "s/$(lsb_release -sc) main/$(lsb_release -sc) main contrib non-
free/" /etc/apt/sources.list  
  
# accepts Microsoft EULA agreement without prompting  
# view EULA at http://wwww.microsoft.com/typography/fontpack/eula.htm  
RUN { echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true; } | debconf-set-selections \  
&& apt-get update && apt-get install -y ttf-mscorefonts-installer  
  
# install packages  
RUN apt-get update && apt-get install -y \  
mysql-common \  
mysql-client \  
libmysqlclient*-dev \  
libgdbm-dev \  
libperl-dev \  
libxml2-dev \  
memcachedb \  
libmemcached-dev \  
libevent-dev \  
acedb-other-dotter \  
make \  
curl \  
gcc \  
php5-gd \  
freetype* \  
libgd2-xpm-dev \  
openssl \  
libssl-dev \  
graphviz \  
libcurl4-openssl-dev \  
default-jre \  
cpanminus \  
vcftools \  
tabix \  
libhts1 \  
libhts-dev  
  
WORKDIR /tmp  
RUN wget -q http://apache.mirror.anlx.net/httpd/CHANGES_2.2 \  
&& export APACHEVERSION=`grep "Changes with" CHANGES_2.2 | head -n 1 | cut -d"
" -f 4` \  
&& wget -q http://apache.mirror.anlx.net/httpd/httpd-$APACHEVERSION.tar.gz \  
&& tar xzf httpd-$APACHEVERSION.tar.gz \  
&& cd httpd-$APACHEVERSION \  
&& ./configure --with-included-apr --enable-deflate --enable-headers --enable-
expires --enable-rewrite --enable-proxy \  
&& make && make install  
  
# install the latest version of mod_perl  
WORKDIR /tmp  
RUN wget -q -O tmp.html http://www.cpan.org/modules/by-module/Apache2/ \  
&& MODPERLTAR=`grep -oP "mod_perl.*?tar" tmp.html | sort -Vr | head -n 1` \  
&& MODPERLVERSION=${MODPERLTAR%.*} \  
&& wget http://www.cpan.org/modules/by-module/Apache2/$MODPERLVERSION.tar.gz \  
&& tar xzf $MODPERLVERSION.tar.gz \  
&& cd $MODPERLVERSION \  
&& perl Makefile.PL MP_APXS=/usr/local/apache2/bin/apxs \  
&& make && make install  
  
RUN apt-get install -y git  
  
# install Tabix.pm  
WORKDIR /tmp  
RUN git clone https://github.com/samtools/tabix  
WORKDIR /tmp/tabix/perl  
RUN perl Makefile.PL \  
&& make && make install  
  
# install Htslib.pm  
WORKDIR /tmp  
RUN git clone https://github.com/samtools/htslib  
WORKDIR /tmp/htslib  
RUN make && make install  
  
RUN apt-get install -y libio-socket-ssl-perl  
  
# install most required perl modules using cpanminus  
RUN cpanm Scalar::Util \  
WWW::Curl::Multi \  
Archive::Zip \  
CGI::Session \  
Class::Accessor \  
CSS::Minifier \  
DBI \  
HTTP::Date \  
Image::Size \  
Inline IO::Scalar \  
IO::Socket \  
IO::Socket::INET \  
IO::Socket::UNIX \  
IO::String \  
List::MoreUtils \  
Mail::Mailer \  
Math::Bezier \  
MIME::Types \  
PDF::API2 \  
RTF::Writer \  
Spreadsheet::WriteExcel \  
Sys::Hostname::Long \  
Text::ParseWords \  
URI \  
URI::Escape \  
HTML::Template \  
Clone \  
Hash::Merge \  
Class::DBI::Sweet \  
Compress::Bzip2 \  
Digest::MD5 \  
File::Spec::Functions \  
HTML::Entities \  
IO::Uncompress::Bunzip2 \  
XML::Parser \  
XML::Simple \  
XML::Writer \  
SOAP::Lite \  
GD \  
GraphViz \  
String::CRC32 \  
Cache::Memcached::GetParser \  
Inline::C \  
XML::Atom \  
LWP \  
BSD::Resource \  
JSON \  
Linux::Pid \  
Readonly \  
Module::Build \  
Bio::Root::Build \  
Lingua::EN::Inflect \  
YAML \  
Math::Round \  
Rose::DB::Object::Manager  
  
# install kent utils (see
https://hub.docker.com/r/genomicpariscentre/biotoolbox/~/dockerfile/ for
inspiration)  
WORKDIR /usr/local  
#RUN git clone git://genome-source.cse.ucsc.edu/kent.git  
RUN wget http://hgdownload.cse.ucsc.edu/admin/jksrc.zip  
RUN apt-get install unzip  
RUN unzip jksrc.zip  
RUN rm jksrc.zip  
  
WORKDIR /usr/local/kent/src/  
ENV MACHTYPE x86_64  
ENV KENT_SRC /usr/local/kent/src  
  
WORKDIR /usr/local/kent/src/inc  
RUN mkdir /usr/local/bin/script; mkdir /usr/local/bin/x86_64  
RUN sed -i "s/CFLAGS\=/CFLAGS\=\\-fPIC/" common.mk \  
&& sed -i "s:BINDIR =
\${HOME}/bin/\${MACHTYPE}:BINDIR=/usr/local/bin/\${MACHTYPE}:" common.mk \  
&& sed -i "s:SCRIPTS=\${HOME}/bin/scripts:SCRIPTS=/usr/local/bin/scripts:"
common.mk  
  
WORKDIR /usr/local/kent/src/lib  
RUN make  
  
WORKDIR /usr/local/kent/src/jkOwnLib  
RUN make  
  
WORKDIR /usr/local/kent/src/htslib  
RUN sed -i "s/-DUCSC_CRAM/-DUCSC_CRAM -fPIC/" Makefile  
RUN make  
  
WORKDIR /tmp  
RUN wget http://cpan.metacpan.org/authors/id/L/LD/LDS/Bio-BigFile-1.07.tar.gz  
RUN tar xzf Bio-BigFile-1.07.tar.gz  
WORKDIR /tmp/Bio-BigFile-1.07  
RUN ls -la \  
&& sed -i "s/\$ENV{KENT_SRC}/\'\/usr\/local\/kent\/src\'/" Build.PL \  
&& sed -i "s/\$ENV{MACHTYPE}/x86_64/" Build.PL \  
&& sed -i 's:extra_linker_flags => \\["\$jk_lib/\$LibFile":extra_linker_flags
=> \\["-pthread","\$jk_lib/\$LibFile","\$jk_include/../htslib/libhts.a":'
Build.PL \  
# && cat Build.PL  
&& perl Build.PL \  
&& ./Build \  
&& ./Build test \  
&& ./Build install  
  
# install Bio::DB::HTS::Tabix using cpanminus  
RUN cpanm Bio::DB::HTS::Tabix  
  
RUN mkdir -p /ensembl  
RUN mkdir -p /ensembl/logs  
RUN mkdir -p /ensembl/tmp  
RUN mkdir -p /ensembl/scripts  
RUN mkdir -p /ensembl/conf  
  
RUN adduser --disabled-password --gecos '' eguser  
  
EXPOSE 8080  
RUN chown -R eguser:eguser /ensembl  
  
# create symbolic link to perl binary in location referenced by ensembl
scripts  
RUN ln -s /usr/bin/perl /usr/local/bin/perl  
  
USER eguser  
COPY update.sh /ensembl/scripts/  
COPY default.setup.ini /ensembl/conf/setup.ini  
RUN /ensembl/scripts/update.sh /ensembl/conf/setup.ini  
COPY *.sh /ensembl/scripts/  
  
WORKDIR /ensembl  
CMD ["/ensembl/scripts/startup.sh"]  
  

