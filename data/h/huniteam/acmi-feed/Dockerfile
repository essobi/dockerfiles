FROM nginx  
  
ENV BASEDIR=/app  
  
ENV SRCDIR=$BASEDIR/collection \  
DESTDIR=/usr/share/nginx/html \  
PERL5LIB=$BASEDIR/lib  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
cpanminus \  
git \  
&& cpanm -q \  
Cpanel::JSON::XS \  
Data::Dumper::Concise \  
Function::Parameters \  
Log::Any \  
Moo \  
Path::Tiny \  
&& rm -rf /root/.cpanm /var/lib/apt/lists  
  
RUN git clone https://github.com/ACMILabs/collection.git $SRCDIR  
  
COPY image/ /  
CMD $BASEDIR/entrypoint.sh  

