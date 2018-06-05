# FROM buildpack-deps:precise  
FROM ubuntu:12.04  
MAINTAINER Bo Gao <bogao@dcs.warwick.ac.uk>  
  
# A. Install OS-level dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
procps \  
ncbi-blast+ \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
## Ref: https://github.com/docker-library/buildpack-
deps/blob/e7534be05255522954f50542ebf9c5f06485838d/precise/Dockerfile  
# B. Install Perl modules  
## B1. CPAN modules  
RUN cd /usr/src \  
&& curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
\  
&& chmod +x cpanm \  
&& ./cpanm App::cpanminus \  
&& rm -fr ./cpanm /root/.cpanm /usr/src/perl /tmp/*  
  
# RUN curl -L https://cpanmin.us | perl - --sudo App::cpanminus  
# RUN cpan App::cpanminus  
RUN mkdir /apples  
ADD ./cpanfile /apples/cpanfile  
RUN cd /apples \  
&& cpanm --notest --installdeps .  
  
## B2. Non-CPAN modules (Ensemble API, Ensemblegenomes API and BioPerl)  
# Ref: https://github.com/bogaotory/docker-perl-bio  
ENV LIB_NCPAN_PERL /root/lib-perl  
  
RUN mkdir $LIB_NCPAN_PERL  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd $LIB_NCPAN_PERL \  
&& git clone https://github.com/Ensembl/ensembl-git-tools.git \  
&& echo 'export PATH="'$LIB_NCPAN_PERL'/ensembl-git-tools/bin:$PATH"' >>
/root/.profile  
  
RUN . /root/.profile \  
&& cd $LIB_NCPAN_PERL \  
&& git ensembl --clone api \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl/modules:$PERL5LIB"' >>
/root/.profile \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-
compara/modules:$PERL5LIB"' >> /root/.profile \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-
funcgen/modules:$PERL5LIB"' >> /root/.profile \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-io/modules:$PERL5LIB"' >>
/root/.profile \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-
variation/modules:$PERL5LIB"' >> /root/.profile  
  
RUN cd $LIB_NCPAN_PERL \  
&& git clone git://github.com/bioperl/bioperl-live.git \  
&& git clone https://github.com/bioperl/Bio-EUtilities.git \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/bioperl-live:$PERL5LIB"' >>
/root/.profile \  
&& echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/Bio-EUtilities/lib:$PERL5LIB"' >>
/root/.profile  
  
# ENV HOSTNAME=gs  
ENV PERL5LIB $LIB_NCPAN_PERL/ensembl/modules:$LIB_NCPAN_PERL/ensembl-
compara/modules:$LIB_NCPAN_PERL/ensembl-
funcgen/modules:$LIB_NCPAN_PERL/ensembl-io/modules:$LIB_NCPAN_PERL/ensembl-
variation/modules:$LIB_NCPAN_PERL/bioperl-live:$LIB_NCPAN_PERL/Bio-
EUtilities/lib  
  
# C. Install Conservation module dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
samtools  
  
RUN cd /tmp \  
&& wget
https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
\  
&& tar -zxvf bedtools-2.25.0.tar.gz \  
&& cd bedtools2 \  
&& make \  
&& make install  
  
RUN wget https://www.python.org/ftp/python/3.4.5/Python-3.4.5.tar.xz \  
&& tar xJf ./Python-3.4.5.tar.xz \  
&& cd Python-3.4.5 \  
&& ./configure --prefix=/opt/python3.4 \  
&& make \  
&& make install \  
&& ln -s /opt/python3.4/bin/python3.4 /usr/bin/python3.4 \  
&& ln -s /opt/python3.4/bin/python3 /usr/bin/python3  
  
RUN /opt/python3.4/bin/easy_install-3.4 numpy \  
&& /opt/python3.4/bin/easy_install-3.4 pandas  
  
# Seaweeds dependencies  
RUN apt-get install -y --no-install-recommends \  
libtbb-dev \  
libboost-regex1.48.0 \  
libboost-program-options1.48.0  
  
# D. Patches  
# D1. Install a missing module  
# Since release 1.7.0 Bio::Perl removed Bio::SearchIO::blastxml  
# So we have to install this mobule (required by the rbh module) manually  
# For more info see https://github.com/bioperl/bioperl-
live/releases/tag/release-1-7-0  
RUN cpanm Bio::SearchIO::blastxml  
  
# Finally  
ADD . /apples  

