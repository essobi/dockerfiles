FROM nginx  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
cpanminus \  
libssl-dev \  
openssl \  
zlib1g-dev \  
&& cpanm -q \  
Module::Install  
  
RUN cpanm -q \  
Cpanel::JSON::XS \  
Data::Dumper::Concise \  
Function::Parameters \  
Furl \  
HTTP::Message \  
IO::Socket::SSL \  
Log::Any \  
Moo \  
Path::Tiny \  
URI::Escape  
  
  
ENV BASEDIR=/app  
  
ENV SOLRURL=https://huni.net.au/solr/select \  
DESTDIR=/usr/share/nginx/html \  
PERL5LIB=$BASEDIR/lib  
  
COPY image/ /  
CMD $BASEDIR/entrypoint.sh  

