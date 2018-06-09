# JBrowse  
# VERSION 1.0  
FROM nginx  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update --fix-missing  
RUN apt-get --no-install-recommends -y install git build-essential zlib1g-dev
libxml2-dev libexpat-dev postgresql-client libpq-dev  
  
RUN mkdir -p /jbrowse/ && git clone \--recursive
https://github.com/gmod/jbrowse /jbrowse/ && \  
cd /jbrowse/ && \  
git checkout 1.12.1-release  
  
WORKDIR /jbrowse/  
RUN ./setup.sh && \  
./bin/cpanm --force JSON Hash::Merge PerlIO::gzip Devel::Size \  
Heap::Simple Heap::Simple::XS List::MoreUtils Exception::Class Test::Warn
Bio::Perl \  
Bio::DB::SeqFeature::Store File::Next Bio::DB::Das::Chado && \  
rm -rf /root/.cpan/  
  
RUN perl Makefile.PL && make && make install  
RUN rm -rf /usr/share/nginx/html && ln -s /jbrowse/ /usr/share/nginx/html  
  
VOLUME /data  
COPY docker-entrypoint.sh /  
CMD ["/docker-entrypoint.sh"]  

