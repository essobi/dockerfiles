FROM ubuntu:wily  
# ...  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y install gcc wget  
RUN apt-get -y install make cpanminus perl-tk perl-modules libtest-simple-perl
libperl-ostype-perl libversion-perl libversion-requirements-perl libmodule-
metadata-perl libmodule-build-perl libjson-pp-perl  
RUN apt-get -y install libfile-which-perl libtext-iconv-perl libtext-
micromason-perl libtie-ixhash-perl libsyntax-highlight-engine-simple-perl
libxml-namespacesupport-perl libxml-sax-base-perl libxml-sax-perl libxml-
libxml-perl libxml-libxslt-perl  
RUN apt-get -y install libxml-nodefilter-perl libxml-libxml-iterator-perl
libxml-filter-buffertext-perl libxml-sax-writer-perl libxml-writer-perl
libparse-recdescent-perl libgraph-perl libperlio-gzip-perl libarchive-zip-perl
libio-string-perl  
RUN apt-get -y install libclass-inspector-perl libfile-sharedir-perl
libreadonly-perl libfont-ttf-perl libpdf-api2-perl libxml2-dev  
RUN cpanm UNIVERSAL::DOES XML::CompactTree XML::CompactTree::XS  
RUN cpanm -f Treex::PML  
RUN cpanm Moose MooseX::Getopt MooseX::NonMoose MooseX::Params::Validate
MooseX::SemiAffordanceAccessor Readonly Treex::PML File::Slurp File::HomeDir
File::Path File::ShareDir LWP::Simple Data::Dumper Module::Reload
Locale::Language  
RUN cpanm -f Parse::RecDescent  
RUN cpanm Cwd Scalar::Util autodie String::Util  
RUN cpanm -f PerlIO::Util  
RUN cpanm File::ShareDir::Install File::chdir YAML IO::Interactive
PerlIO::via::gzip Test::Output Test::YAML Test::Base Algorithm::Diff
Text::Diff Spiffy Capture::Tiny  
RUN cpanm -f Treex::Core  
RUN cpanm --installdeps Treex::Unilang  
RUN cpanm -f Treex::Unilang  
RUN cpanm Treex::EN  
  
ENV GIT_SSL_NO_VERIFY=true  
RUN apt-get -y install git  
RUN mkdir -p ~/tectomt && cd ~/tectomt && git clone
https://github.com/ufal/treex.git  
  
RUN cpanm Lingua::Interset  
RUN cpanm Text::Iconv  
RUN cpanm Ufal::NameTag  
  
RUN mkdir -p /root/tectomt/share/data/models/morce/en/  
RUN cd /root/tectomt/share/data/models/morce/en/ && \  
wget
http://ufallab.ms.mff.cuni.cz/tectomt/share/data/models/morce/en/morce.alph  
RUN cd /root/tectomt/share/data/models/morce/en/ && \  
wget
http://ufallab.ms.mff.cuni.cz/tectomt/share/data/models/morce/en/morce.dct  
RUN cd /root/tectomt/share/data/models/morce/en/ && \  
wget http://ufallab.ms.mff.cuni.cz/tectomt/share/data/models/morce/en/morce.ft  
RUN cd /root/tectomt/share/data/models/morce/en/ && \  
wget
http://ufallab.ms.mff.cuni.cz/tectomt/share/data/models/morce/en/morce.ftrs  
RUN cd /root/tectomt/share/data/models/morce/en/ && \  
wget
http://ufallab.ms.mff.cuni.cz/tectomt/share/data/models/morce/en/tags_for_form-
from_wsj.dat  
  
ENV SVN_TRUNK=https://svn.ms.mff.cuni.cz/svn/tectomt_devel/trunk  
# password is "public"  
RUN apt-get -y install subversion  
RUN mkdir -p ~/scratch  
RUN svn --username public --password public export $SVN_TRUNK/libs/packaged
~/scratch/packaged  
RUN cd ~/scratch/packaged/Morce-English && perl Build.PL && ./Build && ./Build
install  
ENV PERL5LIB="$PERL5LIB:/usr/local/lib/x86_64-linux-gnu/perl/5.20.2"  
ENV TMT_ROOT=/root/tectomt  
ENV PATH="${TMT_ROOT}/treex/bin:$PATH"  
ENV PERL5LIB="${TMT_ROOT}/treex/lib:${TMT_ROOT}/libs/other:$PERL5LIB"  
ENV PERLLIB=$PERL5LIB  
RUN URL='http://ufal.mff.cuni.cz/tred/tred_2.5049_all.deb'; FILE=`mktemp`;
wget "$URL" -qO $FILE && dpkg -i $FILE  
RUN mkdir -p $TMT_ROOT/share/  
RUN ln -s /opt/tred $TMT_ROOT/share/  
RUN ln -s /tmp $TMT_ROOT/tmp  
RUN echo "tred_dir: $TMT_ROOT/share/tred" >> ~/.treex/config.yaml  
  
# fix treex missing modules  
RUN cpanm App::whichpm  
RUN cpanm URI::Find::Schemeless  
# install tree-tagger model for english  
RUN bash -c "echo \"Mr. Brown, we'll start tagging.\" | treex -Len
Read::Sentences W2A::EN::Tokenize W2A::TagTreeTagger W2A::EN::Lemmatize
Write::CoNLLX"  
# install featurama  
RUN apt-get install -y swig  
RUN apt-get install -y file  
RUN apt-get install -y autoconf automake libtool  
RUN FILE=`mktemp`; wget
http://www.ms.mff.cuni.cz/~kraut6am/featurama/featurama-1.0.tar.gz -qO $FILE
&& cd `dirname $FILE` && tar -zxf $FILE && cd featurama-1.0 && autoreconf
--install && ./configure --enable-perl && make && make install  
ENV PERL5LIB="$PERL5LIB:/usr/local/lib/perl5/x86_64-linux-gnu-thread-multi"  
RUN bash -c "echo \"Mr. Brown, we'll start tagging.\" | treex -Len
Read::Sentences W2A::EN::Tokenize W2A::EN::TagFeaturama W2A::EN::Lemmatize
Write::CoNLLX"  
RUN cd ~/tectomt/treex && git pull  
RUN cpanm --notest URI::Find::Schemeless Text::Iconv AI::MaxEntropy
Cache::Memcached Email::Find XML::Twig String::Util String::Diff
List::Pairwise MooseX::Role::AttributeOverride YAML::Tiny Graph Tree::Trie
Text::Brew App::whichpm  
RUN cd ~/scratch && svn --username public --password public co
https://svn.ms.mff.cuni.cz/svn/tectomt_devel/trunk/install/tool_installation
&& cd tool_installation/NADA && perl Makefile.PL && make && make install  
RUN apt-get update  
RUN apt-get install -y default-jre  
RUN bash -c "echo 'Hello, world' | treex -Len Util::SetGlobal
if_missing_bundles=ignore Read::Text Scen::Analysis::EN Write::CoNLLX"  
RUN cpanm Cache::LRU  
RUN wget -O /root/.tredrc
https://gist.githubusercontent.com/wroberts/183dbd91272e101db966/raw/db5faf7af4255fff3ba5eb5983f7352b58ebcafc/sample-
tredrc  
  
# docker run wroberts/treex bash -c "echo 'Hello, world' | treex Read::Text
language=en Write::Text language=en"  
# docker run wroberts/treex bash -c "echo 'Hello! Mr. Brown, how are you?' |
treex -Len Read::Text W2A::Segment Write::Sentences"  
# docker run wroberts/treex bash -c "echo 'Hello! Mr. Brown, how are you?' |
treex -Len Read::Text W2A::EN::Segment Write::Sentences"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::TokenizeOnWhitespace Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::Tokenize Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::EN::Tokenize Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::EN::TagLinguaEn Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::EN::Tokenize W2A::TagTreeTagger
W2A::EN::Lemmatize Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::EN::Tokenize W2A::EN::TagFeaturama
W2A::EN::Lemmatize Write::CoNLLX"  
# docker run wroberts/treex bash -c "echo \"Mr. Brown, we'll start tagging.\"
| treex -Len Read::Sentences W2A::EN::Tokenize W2A::EN::TagMorce
W2A::EN::Lemmatize Write::CoNLLX"  
# socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &  
# ifconfig vboxnet0  
# docker run --rm -e DISPLAY=192.168.99.1:0 -i -t -v
/Users/wroberts/Documents/Berlin/qtleap/docker/tred/sshfs:/clou wroberts/treex
ttred  
#  
#
http://www.larkinweb.co.uk/computing/mounting_file_systems_over_two_ssh_hops.html  
#  
# cd /Users/wroberts/Documents/Berlin/qtleap/docker/tred  
# mkdir -p sshfs  
# ssh -f amor -L 2222:clou:22 -N  
# sshfs -p 2222 robertsw@localhost:/work/robertsw/qtleap/qtleap sshfs  

