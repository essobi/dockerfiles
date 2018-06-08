# JBrowse  
# VERSION 1.0  
FROM httpd  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG JBROWSE_VER=1.12.1-release  
  
RUN apt-get -qq update --fix-missing  
RUN apt-get --no-install-recommends -y install git build-essential zlib1g-dev
libxml2-dev libexpat-dev postgresql-client libpq-dev ca-certificates nano less  
  
RUN mkdir -p /jbrowse/ && git clone \--recursive
https://github.com/gmod/jbrowse /jbrowse/ && \  
cd /jbrowse/ && \  
git checkout ${JBROWSE_VER}  
  
WORKDIR /jbrowse/  
  
RUN ./setup.sh && \  
./bin/cpanm --force JSON Hash::Merge PerlIO::gzip Devel::Size \  
Heap::Simple Heap::Simple::XS List::MoreUtils Exception::Class Test::Warn
Bio::Perl \  
Bio::DB::SeqFeature::Store File::Next Bio::DB::Das::Chado && \  
rm -rf /root/.cpan/  
  
RUN perl Makefile.PL && make && make install  
  
WORKDIR $HTTPD_PREFIX  
  
RUN rm -rf /usr/local/apache2/htdocs && ln -s /jbrowse/
/usr/local/apache2/htdocs  
#/usr/share/nginx/html && ln -s /jbrowse/ /usr/share/nginx/html  
VOLUME /data  
COPY docker-entrypoint.sh /  
  
#CMD ["httpd-foreground"]  
CMD ["/docker-entrypoint.sh"]  

